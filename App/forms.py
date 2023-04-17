from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order      # these are fixed and required parameters.
        fields = '__all__' 


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username','email']


class CustomerCreationForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

