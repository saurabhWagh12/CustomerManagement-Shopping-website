from django.contrib import admin
from django.urls import path,include
from .views import *

from django.views.static import serve
from django.conf.urls import url
from majorProject import settings

urlpatterns = [
    path('',home,name='Home'),
    path('<int:id>/',home,name='Home'),
    path('products/',productPage,name='produts'),
    path('customer/<int:cid>/',customerPage,name='customerCust'),
    path('ordered/<int:id>/<int:pid>/',ordering,name='Ordering'),
    path('createOrder/<int:id>/',createOrder,name='createOrder'),
    path('updateOrder/<int:id>/',updateOrder,name='updateOrder'),
    path('deleteOrder/<int:delId>/',deleteOrder,name='deleteOrder'),
    path('login/',loginPage,name='LoginPage'),
    path('register/',register,name='registerPage'),
    path('logout/',loggingOUT,name='logout'),
    path('customerCreation/',createCustomer,name='customerCreation'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]
