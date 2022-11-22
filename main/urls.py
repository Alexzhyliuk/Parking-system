from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='login'),
    path('registr', views.index, name='registr'),
    path('reg_setting', views.index, name='reg_setting'),
    path('personal_area', views.index, name='personal_area'),
    path('about', views.index, name='about'),

]
