from django.db import models

from core.models import BaseMovieModel


class AModelA(BaseMovieModel):
    other_name = "other"

    other = models.ForeignKey("OtherModel", related_name="others", on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ("other", "sequence"),
        )

    def __str__(self):
        return f"{self.id}: {self.other.ticket} - #{self.sequence}"


class OtherModel(models.Model):
    ticket = models.TextField()
