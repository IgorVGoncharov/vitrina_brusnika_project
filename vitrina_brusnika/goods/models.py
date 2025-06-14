from django.db import models

Сhoice_CHOICES = (('Нет', 'Нет'), ('Да', 'Да'))

# Create your models here.
class Chapters(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
            # db_table: 'Chapter'
            verbose_name='Статью'
            verbose_name_plural='Статья'

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL')
    chapter = models.ForeignKey(Chapters, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(upload_to='category_images', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        verbose_name='Категорию'
        verbose_name_plural='Категории'

    def __str__(self):
        return f'{self.name} (категория: {self.chapter})'
    
class Goods(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL')
    info_4_search = models.CharField(max_length=150, default='', verbose_name='Отображаемая информация')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    choice = models.CharField(max_length=50, choices=Сhoice_CHOICES ,default="Нет", verbose_name='Новые товары')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    xs_count = models.PositiveIntegerField(default=0, verbose_name='Количество размера XS')
    s_count = models.PositiveIntegerField(default=0, verbose_name='Количество размера S')
    m_count = models.PositiveIntegerField(default=0, verbose_name='Количество размера M')
    l_count = models.PositiveIntegerField(default=0, verbose_name='Количество размера L')
    xl_count = models.PositiveIntegerField(default=0, verbose_name='Количество размера XL')
    
    

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'

    def __str__(self):
        return self.name
    
    def display_id(self):
        return f'{self.id:05}'
    
    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price*self.discount/100), 2)
        return self.price