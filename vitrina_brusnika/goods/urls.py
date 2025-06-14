from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "goods"

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('product/<slug:slug>/', views.product, name='product')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


