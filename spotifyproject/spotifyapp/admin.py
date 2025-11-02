from django.contrib import admin
from .models import Artist, Genre, Album, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Album)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "cover", "artist",)
    search_fields = ("title",)

@admin.register(Genre)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)

@admin.register(Song)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "artist", "album", "genre",)
    search_fields = ("title",)
