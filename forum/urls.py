# forum/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<int:category_id>/', views.topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', views.post_list, name='post_list'),
    path('reply/<int:post_id>/', views.reply_post, name='reply_post'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
]
