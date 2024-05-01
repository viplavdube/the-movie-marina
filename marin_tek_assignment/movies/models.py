from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster = models.URLField()
    genres = models.CharField(max_length=200)  # Simplified for example; consider a ManyToMany field in a real-world app
    rating = models.FloatField()
    year_release = models.IntegerField()
    metacritic_rating = models.IntegerField()
    runtime = models.IntegerField()

    def __str__(self):
        return self.title

