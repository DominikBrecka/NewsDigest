from django.contrib import admin
from core import models


# Register your models here.
@admin.register(models.NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ("name", "rss_url", "active")


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "source", "published")


class DigestArticleInline(admin.TabularInline):
    model = models.DigestArticle
    extra = 1


@admin.register(models.Digest)
class DigestAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    inlines = [DigestArticleInline]

@admin.register(models.DigestArticle)
class DigestArticleAdmin(admin.ModelAdmin):
    list_display = ("digest", "article")
