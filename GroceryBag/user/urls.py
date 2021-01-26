from django.contrib import admin
from django.urls import path
from user import views

app_name='user'
urlpatterns = [
    
    
    path('userhome/',views.userhome,name='uhome'),
    path('add/',views.add,name='add'),
    path('update/<int:id>',views.gupdate,name='gupdate'),
    path('userhome/filter',views.filter,name='filhome'),
    path('userhome/delete/<int:id>',views.delete,name='delete'),
    
    
]