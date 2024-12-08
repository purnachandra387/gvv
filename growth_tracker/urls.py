from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.plant_growth_log_list, name='plant_growth_log_list'),
    path('add/', views.add_plant_growth_log, name='add_plant_growth_log'),
]