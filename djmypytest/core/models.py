from django.db import models


class MovieManager(models.Manager):
    def movie_method(self):
        pass


class BaseMovieModel(models.Model):
    title = models.TextField()
    sequence = models.IntegerField()

    objects = MovieManager()

    class Meta:
        abstract = True
