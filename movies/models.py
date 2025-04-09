from django.db import models


class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()