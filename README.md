# CRM & Inventory Hub

A minimalist full-stack CRM and Inventory management web application built with Django, HTMX, and PostgreSQL. Deployed on Railway with Docker and GitHub Actions CI/CD.

🔗 **Live App:** https://inventory-hub-production-6e00.up.railway.app

---

## Features

- Full CRUD for Clients, Inventory Items, and Orders
- HTMX-powered live search (no page reload)
- Dynamic inline modals for editing
- Low stock dashboard warning
- Role-based access control via `StaffOnlyMixin`
- Rate-limited login (5 attempts per minute per IP)
- Authenticated navigation with role-based visibility
- Dockerised with GitHub Actions CI/CD pipeline

---

## Tech Stack

- **Backend:** Django 5.x, PostgreSQL
- **Frontend:** HTMX, Tailwind CSS v4
- **Auth & Security:** Django Auth, django-ratelimit
- **Deployment:** Docker, Railway, GitHub Actions, WhiteNoise, Gunicorn

---

## Demo Access

A read-only staff account is available for visitors:

| Username | Password |
|----------|----------|
| staffuser | My2,User |

This account has view-only access to:
- `/client-list/` — All Clients
- `/item-list/` — All Inventory Items
- `/order-list/` — All Orders

Create, Update, and Delete actions are restricted via `StaffOnlyMixin`.

---

## Local Development

### Prerequisites
- Python 3.13
- PostgreSQL
- Docker Desktop (optional)

### Setup

```bash
git clone https://github.com/rposeidon1/inventory-hub.git
cd inventory-hub
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the root:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
```

Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

---

## Deployment

Deployed on Railway using Docker. Environment variables are managed via Railway's dashboard. GitHub Actions handles automated deployment on every push to `main`.

---

## Roadmap

This project will be revisited in Phase 12 to add:
- Email verification
- Background job processing (Celery)
- Payment integration (Paystack)
- reCAPTCHA on login

---

## Author

**Ashfall** — [@rposeidon1](https://github.com/rposeidon1)

Currently working through a structured 14-phase full-stack engineering curriculum covering Django, HTMX, DRF, PostgreSQL, Docker, Flutter, Pytest, and Playwright.
```
