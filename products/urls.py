from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.specific_product, name='specific_product'),
    path('create/', views.create_product, name='create_product'),
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    path(
        'delete/<int:product_id>',
        views.delete_product,
        name='delete_product'
    ),
]
