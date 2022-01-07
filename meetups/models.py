from django.db import models


class Location(models.Model):
    name: str = models.CharField(max_length=200)
    address: str = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Meetup(models.Model):
    title: str = models.CharField(max_length=100)
    description: str = models.TextField()
    slug: str = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images', default='')
    location: Location = models.ForeignKey(to=Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} - {self.title} '
