from django.urls import path
from .views import home, products, story, contact, process

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('story/', story, name='story'),
    path('contact/', contact, name='contact'),
    path('process/', process, name='process'),
]