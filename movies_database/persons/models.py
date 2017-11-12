from django.db import models


class Person(models.Model):
    first_name = models.CharField(
        max_length=64,
    )
    second_name = models.CharField(
        max_length=64,
    )
    year_of_birth = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.second_name)
