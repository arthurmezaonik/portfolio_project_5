from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter_sign_up, name='sign_up'),
]
