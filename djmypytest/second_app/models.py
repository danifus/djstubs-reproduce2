from django.db import models

from test_app.models import OtherModel


class SecondModel(models.Model):
    other = models.ForeignKey(OtherModel, on_delete=models.CASCADE)


hi: int = "hi"
