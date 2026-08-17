import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def estimate(work_hours, integration_hours, streams, efficiency, growth):
    productive = work_hours / (streams * efficiency)
    integration = integration_hours * (1 + growth * (streams - 1))
    return round(productive + integration, 1)


def build_rows(model):
    rows = []
    for code, complexity in model["complexity_classes"].items():
        estimates = []
        for streams in range(1, 6):
            estimates.append(estimate(
                complexity["work_hours"], complexity["integration_base_hours"], streams,
                model["stream_efficiency"][str(streams)], model["integration_growth_per_extra_stream"],
            ))
        rows.append((code, complexity, estimates))
    return rows


def main():
    model = json.loads((ROOT / "registry/capacity_model.json").read_text(encoding="utf-8"))
    rows = build_rows(model)
    lines = [
        "# Прогноз мощности потоков", "", "> Плановая модель 1.0; не является фактической телеметрией.", "",
        "| Класс | Базовый объём | 1 поток | 2 потока | 3 потока | 4 потока | 5 потоков | Ускорение 5/1 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for code, complexity, values in rows:
        speedup = values[0] / values[4]
        lines.append(f"| {code} · {complexity['name']} | {complexity['work_hours']} ч | " +
                     " | ".join(f"{value} ч" for value in values) + f" | {speedup:.2f}× |")

    book_work, book_integration = 48, 4
    one = estimate(book_work, book_integration, 1, model["stream_efficiency"]["1"], model["integration_growth_per_extra_stream"])
    five = estimate(book_work, book_integration, 5, model["stream_efficiency"]["5"], model["integration_growth_per_extra_stream"])
    lines.extend([
        "", "## Текущий пример BOOK KB", "",
        f"Известная плановая трудоёмкость трёх слоёв — {book_work} ч. При условной интеграции {book_integration} ч "
        f"модель даёт **{one} ч одним потоком** и **{five} ч пятью потоками**, то есть ускорение около **{one / five:.2f}×**.",
        "", "Это расчёт при возможности безопасно разделить работу. Если все потоки изменяют одни и те же файлы, "
        "срок может увеличиться из-за конфликтов.", "",
    ])
    report_dir = ROOT / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "CAPACITY_ESTIMATE.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
