from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'director', 'release_date', 'rating')
    list_filter = ('genre',)
    search_fields = ('name', 'director')
