# Learning Log — Django course tutorial project

This project recreates the **Learning Log** app demonstrated in Django Parts I–VIII and the provided HTML templates. It uses the same MainApp and users app structure, Topic/Entry models, owner-only journal entries, Bootstrap 4 appearance, and Django user authentication. It intentionally does **not** include Campus SkillSwap marketplace features.

## Start on Windows (VS Code PowerShell)

1. Extract the ZIP into a **new** folder (do not overwrite Campus SkillSwap).
2. Open that folder in VS Code.
3. Open Terminal and run:

```powershell
py -m venv django_venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\django_venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

4. Open http://127.0.0.1:8000/ and register a new account.

If port 8000 is already in use, stop the previous Django server with Ctrl+C.

## Test

```powershell
python manage.py test
python manage.py check
```

## Admin (optional)

```powershell
python manage.py createsuperuser
```

Visit http://127.0.0.1:8000/admin/.

## Features

- Homepage and Bootstrap 4 navigation
- Registration, login, and POST logout
- Personal topics and journal entries
- Create topics, create entries, edit entries
- Users cannot view or modify other users' topics/entries, including direct URLs
- SQLite database and Django admin

## Notes

- Bootstrap 4 is loaded from a CDN instead of the older `django-bootstrap4` template library used in the professor's examples, to simplify Django 5.2 compatibility. The provided HTML templates are reused where possible.
- The logout button uses a POST form because modern Django requires POST for logout.
- The project is configured for **local development only**, not public deployment. The professor's Part VIII covers Render deployment, which would require additional production configuration.
- The SQLite database is created when you run `migrate` and is not included in the ZIP.
