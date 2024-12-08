from django.urls import path
from .views import view_tips

app_name = 'tips'

urlpatterns = [
    path('view/', view_tips, name='view_tips'),
]
