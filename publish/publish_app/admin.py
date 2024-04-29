from django.contrib import admin
from .models import Term, News, Article, HistoricalEvent, Quote, Image

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')

@admin.register(HistoricalEvent)
class HistoricalEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)
    search_fields = ('title', 'description')

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'source')
    search_fields = ('text', 'author')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'description', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('description',)