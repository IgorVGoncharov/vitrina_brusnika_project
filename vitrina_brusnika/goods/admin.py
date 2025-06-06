from django.contrib import admin
from goods.models import Chapters, Categories, Goods

# Register your models here.
@admin.register(Chapters)
class ChapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)};


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)};

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)};