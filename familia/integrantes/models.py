from django.db import models


class Familiares(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    description = models.CharField(max_length=200, null=True, blank=True)
    date_birth = models.DateField(null=True,)
    
    