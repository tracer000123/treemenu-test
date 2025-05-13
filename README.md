# UpTrader Tree Menu — Test Assignment

Lightweight Django project implementing a dynamic tree‑like menu, rendered with a single DB query via a custom template‑tag.

## Quick start

```bash
git clone <your-fork-url>
cd treemenu_project
python -m venv venv
source venv/bin/activate  # for Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ — the `draw_menu 'main'` tag renders the menu defined in admin.

## Key points

* **1 SQL query** to fetch all `MenuItem`s for a given `Menu`  
* Recursive template includes only expand‑path — active branch stays open  
* Fully self‑contained, no JS / external libs  
* Tested on Django 4.2 & Python 3.12
