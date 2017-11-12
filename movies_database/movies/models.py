# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from persons.models import Person


class Role(models.Model):
    movie = models.ForeignKey(
        Person,
    )
    person = models.ForeignKey(
        'Movie',
    )
    role = models.CharField(
        max_length=32,
        choices=[
            ('actor', 'actor'),
            ('director', 'director'),
        ]
    )

    def __str__(self):
        return '{} - {}'.format(self.movie, self.person)


class Movie(models.Model):
    title = models.CharField(
        max_length=64,
    )
    description = models.TextField()
    actors = models.ManyToManyField(
        Person,
        through=Role,
        limit_choices_to={'role': 'actor'},
    )
    year = models.IntegerField()
    genre = models.CharField(
        max_length=64,
    )

    def __str__(self):
        return '{} {}'.format(self.title, self.year)

