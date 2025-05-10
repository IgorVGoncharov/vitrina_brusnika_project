from django.shortcuts import render
from django.db.models import Q
from goods.models import Goods, Categories

# Create your views here.
def index(request):

    new_goods = Goods.objects.filter(choice = "Да")
    categories = Categories.objects.filter(Q(name = 'Зонты') | Q(name = 'Футболки'))

    context = {
        'title': 'Главная страница',
        'new_goods': new_goods,
        'categories': categories,
    }

    return render(request, 'goods/index.html', context)