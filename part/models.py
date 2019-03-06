from django.db import models
from django.shortcuts import reverse

from movie.models import Movie
from person.models import Person


class Cast(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.DO_NOTHING,
        related_name='cast',
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.DO_NOTHING,
        related_name='cast_member',
    )
    character = models.CharField(
        max_length=32,
    )

    class Meta:
        verbose_name_plural = 'Cast'

    def __str__(self):
        return '{} - {}'.format(self.movie, self.person)

    def get_absolute_url(self):
        return reverse('part:cast-detail', kwargs={'pk': self.pk})


class Crew(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.DO_NOTHING,
        related_name='crew',
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.DO_NOTHING,
        related_name='crew_member',
    )
    department = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    credit = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = 'Crew'

    def __str__(self):
        return '{} - {}'.format(self.movie, self.person)

