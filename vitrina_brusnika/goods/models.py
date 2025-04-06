from django.db import models

# Create your models here.
class Chapter(models.Model):
    name = models.CharField(max_length=100);
    slug = models.SlugField(max_length=100);

class Category(models.Model):
    name = models.CharField(max_length=100);
    slug = models.SlugField(max_length=100);
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

