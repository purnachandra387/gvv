from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('users/', include('users.urls')),
    path('garden/', include('garden.urls')),
    path('reminders/', include('reminders.urls')),
    path('tips/', include('tips.urls')),
    path('forum/', include('forum.urls')),
    path('growth_tracker/', include('growth_tracker.urls')),
    path('admin/', admin.site.urls),
]