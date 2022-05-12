from unicodedata import name
from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('services/', views.service,name='service'),
    path('products/', views.product,name='product'),
    path('blog/', views.updates,name='updates'),
    path('blog-details/<str:slug>/', views.updatesDetails,name='updatesDetails'),
    path('contact/', views.contact,name='contact'),
    path('SaveContactForm/', views.SaveContactForm,name='SaveContactForm')
]