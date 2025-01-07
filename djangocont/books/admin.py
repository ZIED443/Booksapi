
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import *



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'date_release')
    search_fields = ('name', 'author__name')  # Search by book name and author name
    list_filter = ('author', 'date_release')
    ordering = ('date_release',)