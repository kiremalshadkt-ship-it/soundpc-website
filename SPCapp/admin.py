from django.contrib import admin
from .models import Character, Series

# Register your models here.

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'series', 'role')
    list_filter = ('role', 'series')
    search_fields = ('name',)
