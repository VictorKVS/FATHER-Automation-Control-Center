# Текущий статус автоматических потоков

Снимок: `2026-08-17T10:53:18+03:00`

- Мощность: **5**
- Активно: **4**
- Резерв: **1**
- Загрузка: **80%**
- Плановая трудоёмкость известных активных этапов: **48 ч**
- Зафиксировано событий переназначения/управления: **6**

## Активные потоки

| Поток | Назначение | Этап | План, ч | Прогресс |
|---|---|---|---:|---:|
| STREAM-01 · Аудит базы ИБ | Security Knowledge Base | evidence-base expansion and red-team audit | н/д | н/д |
| STREAM-02 · BOOK KB — сущности | Персонажи, места, предметы, организации и стабильные ID | MVP entity contract | 16 | 20% |
| STREAM-03 · BOOK KB — хронология | События, время, места, перемещения, владение и получение информации | MVP chronology contract | 20 | 15% |
| STREAM-04 · BOOK KB — контроль | Проверка канона, тесты, отчёт и подготовка защиты | MVP verification and defense | 12 | 45% |

## Фабрики

| Фабрика | Статус | Потоки | Репозиторий |
|---|---|---:|---|
| Security Knowledge Factory | active | 1 | VictorKVS/KNOWLEDGE_CORE |
| BOOK·CRAFT Knowledge Factory | active-mvp | 3 | planned |
| OSINT Factory | paused | 0 | VictorKVS/OSINT_deepseek |
| FATHER Product Factory | paused | 0 | VictorKVS/PX00 |
| Professional KB Factory | paused | 0 | VictorKVS/KNOWLEDGE_CORE |
| FATHER Engineering Competency Lab | paused | 0 | FATHER-Engineering-Competency-Lab |
| FATHER Media Lab | paused | 0 | VictorKVS/father-media-lab |
| FATHER Quant Lab | redirected | 0 | VictorKVS/father-quant-lab |

## Последние события

| Время | Событие | Было | Стало |
|---|---|---|---|
| 2026-08-17T10:51:38+03:00 | redirect | FATHER Quant Lab | BOOK KB — сущности |
| 2026-08-17T10:51:40+03:00 | redirect | Доклад по FATHER | BOOK KB — хронология |
| 2026-08-17T10:51:39+03:00 | redirect | FATHER Daily Build Report | BOOK KB — контроль |
| 2026-08-17T10:51:37+03:00 | resume | paused | OSINT |
| 2026-08-17T10:53:17+03:00 | pause | OSINT | paused |
| 2026-08-17T10:53:17+03:00 | resume | paused | Security Knowledge Base |

## История использования потоков

| Работа | Фабрика | Потоки | Объём | Сложность | План | Факт | Статус |
|---|---|---:|---|---|---:|---:|---|
| Аудит базы ИБ | Security Knowledge Factory | 1 | XL | critical | н/д | н/д | active |
| DZ-6 M0→M1 ночной цикл | BOOK·CRAFT Knowledge Factory | 1 | M | high | 8 | н/д | completed |
| Автономный Quant Lab | FATHER Quant Lab | 1 | L | high | н/д | н/д | redirected |
| Сущности BOOK KB | BOOK·CRAFT Knowledge Factory | 1 | M | high | 16 | н/д | active |
| Хронология BOOK KB | BOOK·CRAFT Knowledge Factory | 1 | L | high | 20 | н/д | active |
| Контроль BOOK KB | BOOK·CRAFT Knowledge Factory | 1 | M | high | 12 | н/д | active |
| Автономная разработка OSINT | OSINT Factory | 1 | XL | critical | н/д | н/д | paused |

> Фактическое время запусков не вычисляется из расписания. Если телеметрия запуска отсутствует, значение остаётся неизвестным.
