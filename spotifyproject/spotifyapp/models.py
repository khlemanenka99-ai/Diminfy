from django.db import models

class Genre(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='artists/', blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=100, unique=True)
    cover = models.ImageField(upload_to='albums/', blank=True, null=True)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='albums'
    )
    relise_year = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} -- {self.artist.name}"

class Song(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=100)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='songs'
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.SET_NULL,
        related_name='albums',
        blank=True,
        null=True
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='albums',
        blank=True,
        null=True
    )
    audiofile = models.FileField(upload_to='songs/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} -- {self.artist.name}"


