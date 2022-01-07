from typing import List

from django.db import models


class Location(models.Model):
    name: str = models.CharField(max_length=200)
    address: str = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    firstName: str = models.CharField(max_length=50)
    lastName: str = models.CharField(max_length=50, blank=True, null=True)
    email: str = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Meetup(models.Model):
    title: str = models.CharField(max_length=100)
    organizer_email: str = models.EmailField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description: str = models.TextField(blank=True, null=True)
    slug: str = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images', default='', blank=True, null=True)
    location: Location = models.ForeignKey(to=Location, on_delete=models.CASCADE, blank=True, null=True)
    participants: List = models.ManyToManyField(to=Participant, blank=True)

    def __str__(self):
        return f'{self.pk} - {self.title} '
