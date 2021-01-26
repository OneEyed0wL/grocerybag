from django.contrib import admin
from django.urls import path
from home import views

app_name='hom'
urlpatterns = [
    
    
    path('',views.home,name='home'),
    path('user_reg/',views.user_regs,name='user_reg'),
    path('login/',views.login,name='login'),
    
]