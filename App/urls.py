from django.contrib import admin
from django.urls import path,include
from .views import *


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
    path('change/',forgot,name='changepassword'),

]
