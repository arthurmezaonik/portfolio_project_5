from django.contrib import admin
from .models import Product, Collection, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'collection',
        'price',
        'calories',
        'image',
    )

    ordering = ('sku',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'body',
        'product',
        'created_on',
    )

    list_filter = (
        'created_on',
    )

    search_fields = (
        'name',
        'email',
        'body'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Review, ReviewAdmin)