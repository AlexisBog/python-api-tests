# API Testing Framework

Проєкт для тестування JSONPlaceholder REST API за допомогою Python (`requests`) та `pytest`.

## Структура проєкту
- `api/client.py` — Універсальний клієнт для виконання запитів та логування.
- `tests/test_api.py` — Набір модульних тестів (CRUD, негативні тести, headers).
- `conftest.py` — Фікстури для запуску `pytest`.

## Інструкція зі встановлення та запуску

1. Встановіть залежності:
   ```bash
   pip install -r requirements.txt