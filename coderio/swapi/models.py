from django.db import models

from django.db import models

class Swapi(models.Model):
    rating = models.IntegerField(default = 1)
    idcharacter = models.IntegerField()
