from django import forms

from .models import Mockdata

class MockdataForm(forms.MockdataForm):
    class Meta:
        model = Mockdata
        fields = [
            'name',
            'short_name',
            'total_docs',
        ]

# class Mockdata(models.Model):
#     name = models.CharField(max_length=100)
#     short_name = models.CharField(max_length=5)
#     total_docs = models.IntegerField()