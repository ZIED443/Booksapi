# Django bookstore API Project

## Overview

This project is a **modular Django REST Framework API** designed for managing a Bookstore application with user accounts and reservations. It follows a clean architecture, separating **core infrastructure, apps, and API layers** for maintainability, scalability, and testability.

**Key Features:**

- Multi-app structure (`bookstore`, `reservations`, `users`) for modularity.
- RESTful API endpoints with versioning (`api/v1`).
- Signal-based business logic handling (e.g., notifications, auto-updates).
- Robust testing setup for models and signals.
- Environment-specific Django settings for **production**, **testing**, and **development**.
- Swagger/OpenAPI documentation integration.

---

## Architecture

The system follows a modular architecture separating concerns across layers:

- **Core** – Global configuration, environment setup, and shared middlewares.
- **Apps** – Independent Django apps following the Domain-Driven Design (DDD) approach.
- **API Layer** – Versioned endpoints exposing serializers, viewsets, and routers.

This design ensures scalability, testability, and minimal coupling between modules.

## Project Structure

./api/  
├── init.py  
├── v1/  
│ ├── bookstore/  
│ │ ├── serializers.py  
│ │ ├── urls.py  
│ │ └── views.py  
│ ├── reservations/  
│ │ ├── serializers.py  
│ │ ├── urls.py  
│ │ └── views.py  
│ ├── users/  
│ │ ├── serializers.py  
│ │ ├── urls.py  
│ │ └── views.py  
│ └── swagger.py  
│ └── urls.py  
│  
./apps/  
├── bookstore/  
│ ├── models.py  
│ ├── signals.py  
│ ├── apps.py  
│ ├── migrations/  
│ └── tests/  
├── reservation/   
│ ├── models.py  
│ ├── signals.py  
│ ├── apps.py  
│ ├── migrations/  
│ └── tests/  
├── users/  
│ ├── models.py  
│ ├── signals.py  
│ ├── apps.py  
│ ├── migrations/  
│ └── tests/  
└── infrastructure/  
  
./core/  
├── settings/  
│ ├── base.py  
│ ├── prod.py  
│ ├── test.py  
├── urls.py  
├── wsgi.py  
└── asgi.py  
  


## Installation

1. **Clone the repository**

```bash
git clone https://github.com/ZIED443/Booksapi.git
```

2. **Create a python virtual environment**

```bash
python -m venv (env-name) 
```

3. **Set  env**

```bash
ENV_FILE=.env.test
DJANGO_ENV=test    
DJANGO_PORT=
DEBUG=
WEB_CONTAINER_NAME=
EMAIL_PORT=
EMAIL_LOGIN=
EMAIL_PASSWORD=
SECRET_KEY=
GUNICORN_WORKERS=
DB_CONTAINER_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
DB_PORT=
POSTGRES_VOLUME=
```


## Migrations

* Make migrations:

```bash
python manage.py makemigrations
```

* Apply migrations:

```bash
python manage.py migrate
```
## Starting the app
* Running the Project

```bash
python manage.py runserver
```

* API Endpoints:  
  * Base URL:  **/api/v1/**  
  * Swagger documentation:   **/api/v1/swagger/**

##  Running with Docker Compose

The project is fully containerized — you only need a valid .env file.  
All setup steps (database, migrations, static files, etc.) are automatically handled by Docker.The container automatically adapts depending on the value of **`DJANGO_ENV`** in your `.env` file:

| `DJANGO_ENV` value | Behavior |
|--------------------|-----------|
| `test` | Runs Django with the **testing settings** (`core.settings.test`) using `manage.py runserver`. |
| `prod` | Starts the app using **Gunicorn** with the **production settings** (`core.settings.prod`). |

This allows the same **`docker-compose.yml`** to be used for **development**, **testing**, and **production** environments with **no code changes** — just switch the `.env` file.

* **Example `.env` entry:**

```bash
DJANGO_ENV=prod

```
*  Run the entire stack
```bash
docker-compose --env-file (env file ) up  --build
```

## Testing
* Run all tests:

```bash
pytest apps/ --ds=core.settings.test -v
```
* Run tests for a specific app:

```bash
python manage.py test apps.bookstore --settings=core.settings.test
python manage.py test apps.reservations --settings=core.settings.test
python manage.py test apps.users --settings=core.settings.test
```

* Run tests with coverage:

```bash
pytest --cov=apps --cov-report=html apps/ --ds=core.settings.test -v
```

## Contributing
* Follow  DRY, and SOLID principles.

* Write and run tests before pushing code.

* Create feature branches from main.

* Use descriptive commit messages.

## Contact

Created and maintained by **Zied Jemal**  
[Email](mailto:ziedjmal@hotmail.com) - [LinkedIn](https://www.linkedin.com/in/zied-jemal)    

---

## License

This project is licensed under the [MIT License](LICENSE).  
© 2025 – **Zied Jemal**
