from django.db import models

from core.models import BaseMovieModel


class AModelA(BaseMovieModel):
    unrelated_attrib = "hi"

    actor = models.TextField()

    class Meta:
        unique_together = (
            ("title", "sequence"),
        )
