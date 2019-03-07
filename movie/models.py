from django.db import models

from main.utils import generate_slug


class Genre(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
    )

    def __str__(self):
        return '{}'.format(self.name)


class MovieQuerySet(models.QuerySet):

    def with_rating(self):
        return self.annotate(rating=models.Avg('ratings__value'))

    def search(self):
        return self.filter()


class MovieManager(models.Manager):

    def get_queryset(self):
        return MovieQuerySet(self.model, using=self.db)

    def with_rating(self):
        return self.get_queryset().with_rating()

    def search(self, keyword):
        return self.get_queryset().search(keyword)


class Movie(models.Model):
    objects = MovieManager()
    title = models.CharField(
        max_length=64,
    )
    description = models.TextField()

    year = models.IntegerField()
    genre = models.ManyToManyField(
        Genre,
    )
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        generate_slug(self, from_fields=['title', 'year'])
        super().save(*args, **kwargs)

    @property
    def director(self):
        directors_queryset = self.crew.filter(credit='director')
        res = []
        for director in directors_queryset:
            res.append(director.fullname)
        return res

    def __str__(self):
        return '{} {}'.format(self.title, self.year)
