from django.db import models

# Create your models here.
class Mockuser(models.Model):
    name = models.CharField(max_length=100)
    nric = models.IntegerField()
    age = models.IntegerField()

    def _str_(self):
        return self.name