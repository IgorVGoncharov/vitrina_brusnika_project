from django import template
from goods.models import Categories, Chapters

register = template.Library()

@register.simple_tag
def tag_categories(filter=None):
    if not filter:
        return Categories.objects.all()
    else:
        return Categories.objects.filter(chapter__name=filter)

@register.simple_tag
def tag_chapter():
    return Chapters.objects.all()
