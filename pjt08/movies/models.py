from django.db import models
from django.db.models.fields.related import OneToOneField

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()

    def __str__(self):
        return f'{self.pk} {self.title}'


class Actor(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='actors')

    def __str__(self):
        return f'{self.pk} {self.name}'


class Review(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f'{self.pk} {self.title}'
