from django.db import models

from atest_app.models import OtherModel


class SecondManager(models.Manager):
    def something(self, arg):
        hello = ack
        return None


class SecondModel(models.Model):
    other = models.ForeignKey(OtherModel, on_delete=models.CASCADE)

    objects = SecondManager()
