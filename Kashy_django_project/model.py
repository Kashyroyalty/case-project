from django.db import models


class Cases(models.Model):
    phonetype = models.CharField(max_length=50, blank=True, null=False)
    casematerial = models.CharField(max_length=50, blank=True, null=False)
    colour = models.CharField(max_length=50, blank=True, null=False)
    accessories = models.CharField(max_length=50, blank=True, null=False)


def __str__(self):
    return self.name
