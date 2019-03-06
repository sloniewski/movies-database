from django.db import models


from main.utils import generate_slug


class Person(models.Model):
    first_name = models.CharField(
        max_length=64,
    )
    second_name = models.CharField(
        max_length=64,
    )
    year_of_birth = models.IntegerField()

    slug = models.SlugField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('second_name', 'first_name')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.second_name)

    def save(self, *args, **kwargs):
        generate_slug(self, from_fields=['first_name', 'second_name'])
        super().save(*args, **kwargs)

    @property
    def fullname(self):
        return self.__str__()

