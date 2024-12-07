from django.contrib import admin

from wanderly.trips.models import Trip, Note


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_published')
    ordering = ('name', 'is_published')
    search_fields = ('name', 'description')
    list_filter = ('is_published', 'name', 'description')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('category', 'created_at')
    list_filter = ('category', 'content')