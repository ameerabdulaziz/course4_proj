from django.contrib import admin

from .models import SearchTerm, Genre, Movie


@admin.register(SearchTerm)
class SearchTermAdmin(admin.ModelAdmin):
    list_display = ('id', 'term', 'last_search')
    list_filter = ('last_search',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'year',
        'runtime_minutes',
        'imdb_id',
        'plot',
        'is_full_record',
    )
    list_filter = ('is_full_record',)