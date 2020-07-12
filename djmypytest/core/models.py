from django.db import models


class MovieManager(models.Manager):

    def movie_method(self, arg1, arg2):
        pass

    def second_movie_method(self, sequence, **kwargs):
        get_or_create_params = {
            self.model.other_name: kwargs.pop(self.model.other_name),
            "sequence": sequence,
            "defaults": kwargs,
        }
        return self.get_or_create(**get_or_create_params)


class BaseMovieModel(models.Model):
    other_name: str

    title = models.TextField()
    sequence = models.IntegerField()

    objects = MovieManager()

    class Meta:
        abstract = True
