from django.db import models
#from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length = 254)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 254)
    team = models.ForeignKey(Team, related_name='people', on_delete = models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name
