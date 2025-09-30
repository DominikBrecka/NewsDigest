import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsdigest.settings')
app = Celery('newsdigest')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch-articles-every-10-mins': {
        'task': 'core.tasks.fetch_articles',
        'schedule': 10.0,
    },
}

app.conf.timezone = 'UTC'
