from django.shortcuts import reverse
from django.db import models

from persons.models import Person


class Genre(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
    )

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def movies_list_url(self):
        return reverse('genre-movie-list', kwargs={'pk': self.pk})


class Cast(models.Model):
    movie = models.ForeignKey(
        'Movie',
        on_delete=models.DO_NOTHING,
        related_name='cast_movie',
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.DO_NOTHING,
        related_name='cast_person',
    )
    character = models.CharField(
        max_length=32,
    )

    def __str__(self):
        return '{} - {}'.format(self.movie, self.person)

    def get_absolute_url(self):
        return reverse('cast-detail', kwargs={'pk': self.pk})



class Crew(models.Model):
    movie = models.ForeignKey(
        'Movie',
        on_delete=models.DO_NOTHING,
        related_name='crew_movie',
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.DO_NOTHING,
        related_name='crew_person',
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

    def __str__(self):
        return '{} - {}'.format(self.movie, self.person)


class Movie(models.Model):
    title = models.CharField(
        max_length=64,
    )
    description = models.TextField()

    cast = models.ManyToManyField(
        Person,
        through=Cast,
        related_name='movie_cast',
    )
    crew = models.ManyToManyField(
        Person,
        through=Crew,
        related_name='movie_crew',
    )
    year = models.IntegerField()
    genre = models.ManyToManyField(
        Genre,
    )
    rating = models.IntegerField(
        null=True,
        blank=True,
    )

    @property
    def director(self):
        directors_queryset = self.crew.filter(crew_person__credit='director')
        res = []
        for director in directors_queryset:
            res.append(director.fullname)
        return res

    @property
    def url(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.title, self.year)
