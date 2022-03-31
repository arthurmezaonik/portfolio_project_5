from django.contrib import admin
from .models import SigneUp


@admin.register(SigneUp)
class SigneUpAdmin(admin.ModelAdmin):
    """ Register newslleter to admin area """
    list_display = ('email', )
    list_filter = ('email',)
