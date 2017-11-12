from django.db import models


class Person(models.Model):
    first_name = models.CharField(
        max_length=64,
    )
    second_name = models.CharField(
        max_length=64,
    )
    year_of_birth = models.IntegerField()
