from django.urls import path
from . import views

urlpatterns = [
    path('', views.management_area, name='management'),
]
