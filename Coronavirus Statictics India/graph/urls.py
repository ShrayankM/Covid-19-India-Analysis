from django.contrib import admin
from django.urls import path, include
from graph import views

app_name = 'graph'

urlpatterns = [
    path('pie/', views.pie, name = 'pie'),
    path('area/', views.area, name = 'area'),
    path('bar/', views.bar, name = 'bar'),
    path('india_map/', views.india_map, name = 'india'),
]
