from django.db import models

# Create your models here.
class Chapters(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название');
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL');

    class Meta:
            # db_table: 'Chapter'
            verbose_name='Статью'
            verbose_name_plural='Статья'

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название');
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL');
    chapter = models.ForeignKey(Chapters, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name='Категорию'
        verbose_name_plural='Категории'

    def __str__(self):
        return f'{self.name} (категория: {self.chapter})'