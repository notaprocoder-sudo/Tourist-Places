
from django.urls import path
from . import views


app_name = 'tourapp'

urlpatterns = [
    path('', views.Home, name='Home'),
    path('add/',views.add_spot,name='add_spot'),
    path('details/<int:id>/', views.details, name='details'),
    path('edit/<int:id>/', views.edit,name='edit'),
    path('dele/<int:id>/', views.dele, name='dele'),
]