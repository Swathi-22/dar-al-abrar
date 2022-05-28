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
    path('SaveContactForm/', views.SaveContactForm,name='SaveContactForm'),
    path('get-countries/',views.get_product,name="get_product"),
    path('get-price/',views.get_price,name="get_price"),
    path('get-totalprice/',views.get_totalPrice,name='get_totalPrice'),
    path('send-whatsapp/',views.sendWhatsapp,name='sendWhatsapp'),
    path('order-tracking/',views.tracking,name='tracking'),
    path('order-tracking/<str:slug>/',views.live_tracking, name='live_tracking'),
]