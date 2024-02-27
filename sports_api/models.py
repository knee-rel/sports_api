from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):  # creaitng method, to create the spacing in between generated strings
        return self.name + ' ' + self.description
