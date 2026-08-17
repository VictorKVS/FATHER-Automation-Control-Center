# Единый паспорт автоматической задачи

Каждая новая или возобновлённая автоматизация регистрируется до первого запуска.

## Обязательные поля

- `automation_id`, название и фабрика;
- цель и ограниченный этап;
- дата запуска и расписание;
- плановые часы, объём и сложность;
- входные и выходные артефакты;
- критерии MIN/MED/MAX или другой acceptance gate;
- фактическое начало и окончание каждого запуска;
- PASS/FAIL/REWORK и подтверждающие ссылки;
- причина остановки;
- новое назначение при перенаправлении;
- оценка оставшегося времени.

## События жизненного цикла

`create → start → checkpoint → pause/resume → redirect → complete/close`

Операция не удаляет прошлое назначение: перенаправление создаёт новое событие,
а прежняя фабрика сохраняется в `workload_history.csv`.

## Телеметрия запуска

```json
{
  "run_id": "RUN-...",
  "automation_id": "...",
  "started_at": "ISO-8601",
  "finished_at": "ISO-8601",
  "input_volume": {"unit": "documents|entities|tests|requirements", "count": 0},
  "complexity": "low|medium|high|critical",
  "result": "PASS|FAIL|REWORK|BLOCKED",
  "output_count": 0,
  "rework_count": 0,
  "evidence": [],
  "next_gate": "..."
}
```

Без `started_at` и `finished_at` фактическая скорость не рассчитывается.
