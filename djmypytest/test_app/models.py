from django.db import models

from core.models import BaseMovieModel


class ModelA(BaseMovieModel):
    pass


class OtherModel(models.Model):
    ticket = models.TextField()
