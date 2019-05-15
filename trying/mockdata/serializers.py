from rest_framework import serializers
from .models import Mockdata

class MockdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mockdata
        fields = ('id', 'name', 'short_name', 'total_docs')

    # name = models.CharField(max_length=100)
    # short_name = models.CharField(max_length=5)
    # total_docs = models.IntegerField()