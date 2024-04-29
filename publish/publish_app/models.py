from django.db import models
from django.contrib.auth.models import User

class Term(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HistoricalEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"\"{self.text}\" - {self.author or 'Unknown'}"

class Image(models.Model):
    image = models.ImageField(upload_to='misc_images/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description or f"Image {self.id}"

