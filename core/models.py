from django.db import models


# Create your models here.
class NewsSource(models.Model):
    name = models.CharField(max_length=255)
    rss_url = models.URLField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.URLField(unique=True)
    published = models.DateTimeField()
    summary = models.TextField()

    def __str__(self):
        return self.title


class Digest(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name


class DigestArticle(models.Model):
    digest = models.ForeignKey(Digest, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("digest", "article")
