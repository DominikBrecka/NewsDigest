import feedparser
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from celery import shared_task
from .models import NewsSource, Article
from datetime import datetime


@shared_task
def fetch_articles():
    for source in NewsSource.objects.filter(active=True):
        feed = feedparser.parse(source.rss_url)
        for entry in feed.entries:
            link = entry.link
            if not Article.objects.filter(link=link).exists():
                published = None
                if hasattr(entry, "published"):
                    try:
                        published = make_aware(datetime(*entry.published_parsed[:6]))
                    except Exception:
                        published = datetime.now()

                Article.objects.create(
                    source=source,
                    title=entry.title,
                    link=link,
                    published=published,
                    summary=getattr(entry, "summary", ""),
                )
