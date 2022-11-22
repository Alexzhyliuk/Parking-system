from .models import User, Log
from django.forms import ModelForm, TextInput

# class LogForm (ModelForm):
#    class Meta:
#     model = Log
#     fields = ['login', 'password']
#
#     widgets = {
#         "login":TextInput(attrs={
#             'class': 'form-control',
#             'placeholder':'Логин'
#         }),
#         "password": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Пароль'
#         })
#     }