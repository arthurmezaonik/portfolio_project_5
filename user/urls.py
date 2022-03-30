from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_area, name='user_area')
]
