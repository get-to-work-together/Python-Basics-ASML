from rest_framework import serializers

from .models import *


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['code', 'name', 'timezone']

class AirportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Airport
        fields = ['iata', 'name', 'country', 'city']
