from django.db import models

class Сlothes(models.Model):
    clothing_gender = models.CharField(max_length=100)
    clothing_category = models.CharField(max_length=100)
    name_of_cloth = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    clothing_color = models.CharField(max_length=100)
    clothing_size = models.CharField(max_length=100)
    clothing_cost = models.DecimalField(max_digits=8, decimal_places=2)
    clothing_count = models.IntegerField(default=0)
    clothing_image = models.ImageField(upload_to='media/')
    clothing_description = models.TextField()
    clothing_article = models.IntegerField()
    new_collection = models.BooleanField()


