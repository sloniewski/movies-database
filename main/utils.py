import string
from random import shuffle

from rest_framework.pagination import PageNumberPagination
from django.utils.text import slugify


class DefaultPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


def random_string(length=9):
    choice = list(string.ascii_uppercase + string.digits)
    shuffle(choice)
    return ''.join(choice[0:length])


def generate_slug(instance, from_fields=None):
    model = type(instance)
    if not instance.slug:
        if from_fields is not None:
            text = ' '.join(
                [str(getattr(instance, field)) for field in from_fields]
            )
        else:
            text = instance.name
        slug = slugify(text)
        if model.objects.filter(slug=slug).exists():
            slug = slug + '-' + random_string(4)
        instance.slug = slug
        return True
