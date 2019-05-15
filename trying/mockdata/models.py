from django.db import models

# Create your models here.
class Mockdata(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=5)
    total_docs = models.IntegerField()

    def _str_(self):
        return self.short_name