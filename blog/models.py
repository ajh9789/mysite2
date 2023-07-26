from django.db import models


# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_data='publish', allow_unicode=True)
    body = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta :
        ordering = ['created']
        indexs = [
            models.Index(fields=['created'])
        ]
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'