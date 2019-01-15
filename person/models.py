from django.shortcuts import reverse
from django.db import models


class Person(models.Model):
    first_name = models.CharField(
        max_length=64,
    )
    second_name = models.CharField(
        max_length=64,
    )
    year_of_birth = models.IntegerField()

    @property
    def fullname(self):
        return self.__str__()

    @property
    def url(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.first_name, self.second_name)

    class Meta:
        ordering = ('second_name', 'first_name')
