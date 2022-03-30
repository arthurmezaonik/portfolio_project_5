from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:post_id>', views.specific_post, name='post'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
]
