# TestAppHitech


Это простое Django веб-приложение для вашего тестового проекта.

## Предварительные требования

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Начало работы

1. Клонируйте этот репозиторий на вашем локальном компьютере:

```bash
git clone https://github.com/yourusername/your-django-app.git
cd your-django-app

    Откройте файл docker-compose.yml и замените заполнители на ваши учетные данные для PostgreSQL:

yaml

db:
  image: postgres:latest
  environment:
    POSTGRES_DB: mydb
    POSTGRES_USER: mydbuser
    POSTGRES_PASSWORD: mydbpassword
    Соберите и запустите Docker контейнеры:

bash

docker-compose up --build

    Откройте новое окно/вкладку терминала и выполните следующую команду для применения миграций:

bash

docker-compose run web python manage.py migrate

    Откройте веб-приложение в вашем браузере по адресу http://localhost:8000

    Для остановки контейнеров нажмите Ctrl+C в терминале, где запущена команда docker-compose up.

Использование

    Для запуска приложения: docker-compose up
    Для остановки приложения: docker-compose down
    Для применения миграций и выполнения команд управления: docker-compose run web python manage.py <команда>
    Приложение будет доступно по адресу http://localhost:8000
