# Django CRUD Applications

A Django CRUD (Create, Read, Update, Delete) project.

## Project structure

- `CRUD1/` — Django project (settings/urls/wsgi/asgi)
- `webapp/` — Main Django app
- `static/` — Static files (CSS/JS/images)
- `manage.py` — Django management script
- `db.sqlite3` — SQLite database (created after migrations/run; may not be committed)

## Tech stack

- Python
- Django (generated using Django 5.2.5)
- SQLite (default database)
- `django-crispy-forms` (`CRISPY_TEMPLATE_PACK = 'bootstrap4'`)

## Setup (local)

### 1) Clone the repo
```bash
git clone https://github.com/tad12e/Django-CRUD-applications.git
cd Django-CRUD-applications
```

### 2) Create and activate a virtual environment

**Windows (PowerShell)**
```powershell
python -m venv .venv
. .venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

If you have a `requirements.txt`, install from it:
```bash
pip install -r requirements.txt
```

If you *don’t* have `requirements.txt` yet, install the basics:
```bash
pip install django django-crispy-forms crispy-bootstrap4
```

### 4) Run migrations
```bash
python manage.py migrate
```

### 5) Create an admin user (optional)
```bash
python manage.py createsuperuser
```

### 6) Start the server
```bash
python manage.py runserver
```

Open:
- http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Notes

- `DEBUG = True` in `CRUD1/settings.py`, so this is configured for development.
- Default DB is SQLite (`db.sqlite3`).

## License

Add a license if you plan to share/reuse this project.
