from __future__ import unicode_literals

from django.db import models

class MovieManager(models.Manager):
# add movie functions here

class ActorManager(models.Manager):
    def validate_Actor(self, request):
        actor = self.create(first_name=request.POST['first_name']), last_name=request.POST['last_name'], birthdate=request.POST['birthdate']
        return (True, actor)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    released_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MovieManager

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ActorManager
