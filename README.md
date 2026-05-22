![Catty Logo](static/img/logos/catty-100px.png)

# Catty: The Reminders App (Multicontainer version)

*Catty* — это демонстрационное веб-приложение для заметок-напоминаний.  
В данной версии приложение разделено на два Docker-контейнера:
- **db** – база данных MariaDB (персистентный слой через volume)
- **catty-app** – само FastAPI-приложение

Все компоненты оркестрируются с помощью **Docker Compose**.

## Технологии

- Python 3.12, FastAPI, HTMX, Jinja2
- MariaDB 11
- Docker, Docker Compose
- GitHub Actions (CI/CD: линтинг, тесты, сборка образа, деплой на виртуальную машину)

## Требования к окружению

- Установленные **Docker** (Engine 20.10+) и **Docker Compose** (v2 или standalone `docker-compose`)
- Доступ к GitHub Container Registry (ghcr.io) – для скачивания готового образа приложения
- Для ручного деплоя: SSH-доступ к виртуальной машине (course.prafdin.ru, порт 3102, пользователь `password_123`)

## Переменные окружения

Перед запуском через Docker Compose необходимо задать переменные окружения.  
Вы можете поместить их в файл **`.env`** в той же директории, что и `docker-compose.yaml`, или экспортировать вручную.

| Переменная | Описание | Пример значения |
|------------|----------|------------------|
| `IMAGE` | Полное имя образа приложения (в ghcr.io) | `ghcr.io/psevd00/catty-reminders-app:latest` |
| `APP_CONTAINER_NAME` | Имя контейнера приложения | `catty-app` |
| `MARIADB_ROOT_PASSWORD` | Пароль root для MariaDB | `mypass` |
| `MARIADB_USER` | Пользователь MariaDB для приложения | `password_123` |
| `MARIADB_PASSWORD` | Пароль этого пользователя | `mypass` |
| `MARIADB_DATABASE` | Имя базы данных | `catty_reminders` |
| `HOST_DB_PORT` | Порт на хосте для MariaDB | `3306` |
| `CONTAINER_DB_PORT` | Порт внутри контейнера MariaDB | `3306` |
| `HOST_APP_PORT` | Порт на хосте для веб-приложения | `8181` |
| `CONTAINER_APP_PORT` | Порт внутри контейнера приложения | `8181` |
| `DEPLOY_REF` | Ревизия (commit hash) для маркировки деплоя | `manual` или `${{ github.sha }}` |

Все переменные (кроме `DEPLOY_REF`) **обязательны**.

## Запуск приложения вручную (на вашей ВМ)

1. **Клонируйте репозиторий** и перейдите в ветку `lab4`:
   ```bash
   git clone https://github.com/psevd00/catty-reminders-app.git
   cd catty-reminders-app
   git checkout lab4
