from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import *
from .serializers import *





# API views

class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows countries to be viewed or edited.
    """
    queryset = Country.objects.all().order_by('code')
    serializer_class = CountrySerializer
    # permission_classes = [permissions.IsAuthenticated]


class AirportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Airport.objects.all().order_by('iata')
    serializer_class = AirportSerializer
    # permission_classes = [permissions.IsAuthenticated]