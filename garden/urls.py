from django.urls import path
from .views import plan_garden,garden_detail

urlpatterns = [
    path('', plan_garden, name='garden'),
    path('garden/<int:pk>/', garden_detail, name='garden_detail'),
]
