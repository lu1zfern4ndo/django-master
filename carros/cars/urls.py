from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.cars_view, name='cars_list'),
    path('new_car/', views.new_car, name='new_car'),
]
