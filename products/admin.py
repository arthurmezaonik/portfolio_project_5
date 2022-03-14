from django.contrib import admin
from .models import Product, Collection, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'collections',
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
        'post',
        'created_on',
        'approved'
    )

    list_filter = (
        'approved',
        'created_on'
    )

    search_fields = (
        'name',
        'email',
        'body'
    )

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Product, ProductAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Review, ReviewAdmin)