import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main():
    automation_data = load_json("registry/automations.json")
    factory_data = load_json("registry/factories.json")
    streams = automation_data["streams"]
    active = [stream for stream in streams if stream["status"] == "active"]
    reserve = [stream for stream in streams if stream["status"] == "reserve"]
    planned = sum(stream["planned_stage_hours"] or 0 for stream in active)

    with (ROOT / "registry/stream_events.csv").open(encoding="utf-8", newline="") as file:
        events = list(csv.DictReader(file))
    with (ROOT / "registry/workload_history.csv").open(encoding="utf-8", newline="") as file:
        workloads = list(csv.DictReader(file))

    lines = [
        "# Текущий статус автоматических потоков",
        "",
        f"Снимок: `{automation_data['snapshot_at']}`",
        "",
        f"- Мощность: **{automation_data['capacity']}**",
        f"- Активно: **{len(active)}**",
        f"- Резерв: **{len(reserve)}**",
        f"- Загрузка: **{len(active) / automation_data['capacity']:.0%}**",
        f"- Плановая трудоёмкость известных активных этапов: **{planned} ч**",
        f"- Зафиксировано событий переназначения/управления: **{len(events)}**",
        "",
        "## Активные потоки",
        "",
        "| Поток | Назначение | Этап | План, ч | Прогресс |",
        "|---|---|---|---:|---:|",
    ]
    for stream in active:
        plan = stream["planned_stage_hours"] if stream["planned_stage_hours"] is not None else "н/д"
        progress = f"{stream['progress_percent']}%" if stream["progress_percent"] is not None else "н/д"
        lines.append(
            f"| {stream['stream_id']} · {stream['title']} | {stream['assignment']} | "
            f"{stream['stage']} | {plan} | {progress} |"
        )

    lines.extend(["", "## Фабрики", "", "| Фабрика | Статус | Потоки | Репозиторий |", "|---|---|---:|---|"])
    for factory in factory_data["factories"]:
        lines.append(
            f"| {factory['name']} | {factory['status']} | {factory['active_streams']} | "
            f"{factory['repository']} |"
        )

    lines.extend(["", "## Последние события", "", "| Время | Событие | Было | Стало |", "|---|---|---|---|"])
    for event in events[-10:]:
        lines.append(
            f"| {event['event_time']} | {event['event_type']} | "
            f"{event['from_assignment']} | {event['to_assignment']} |"
        )

    lines.extend([
        "", "## История использования потоков", "",
        "| Работа | Фабрика | Потоки | Объём | Сложность | План | Факт | Статус |",
        "|---|---|---:|---|---|---:|---:|---|",
    ])
    for work in workloads:
        planned = work["planned_hours"] or "н/д"
        actual = work["actual_runtime_hours"] or "н/д"
        lines.append(
            f"| {work['assignment']} | {work['factory']} | {work['stream_count']} | "
            f"{work['volume_class']} | {work['complexity']} | {planned} | {actual} | {work['status']} |"
        )

    lines.extend([
        "",
        "> Фактическое время запусков не вычисляется из расписания. Если телеметрия запуска "
        "отсутствует, значение остаётся неизвестным.",
        "",
    ])
    report_dir = ROOT / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "CURRENT_STATUS.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
