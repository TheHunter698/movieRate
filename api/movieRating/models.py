from django.db import models

# Create your models here.

class Movie(models.Model):

    title = models.CharField(max_length=255, null=False)
    director = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.director) 