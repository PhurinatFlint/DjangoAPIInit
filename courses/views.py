from django.shortcuts import render
from rest_framework import viewsets
from .models import WDAPI
from .serializers import WDAPISerializer

class WDAPIView(viewsets.ModelViewSet):
	queryset = WDAPI.objects.all()
	serializer_class = WDAPISerializer