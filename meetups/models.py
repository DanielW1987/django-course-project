from django.db import models


class Meetup(models.Model):
    title: str = models.CharField(max_length=100)
    # location: str = models.CharField(max_length=100)
    description: str = models.TextField()
    slug: str = models.SlugField(unique=True)
