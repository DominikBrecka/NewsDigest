# NewsDigest

A Django project for aggregating articles from RSS feeds, using **Celery** for background tasks, **Redis** as a message broker, and **PostgreSQL** as the database.  

It fetches new articles from configured RSS sources automatically on a schedule.

**Build and start services**

docker compose up --build

**First-time setup**

**Run database migrations:**

docker compose run --rm web python manage.py migrate

**Create superuser for Django admin:**

docker compose run --rm web python manage.py createsuperuser

**Collect static files:**

docker compose run --rm web python manage.py collectstatic --noinput

**You can run it directly:**

docker compose run --rm web python manage.py shell
from core.tasks import fetch_articles
fetch_articles.delay()
