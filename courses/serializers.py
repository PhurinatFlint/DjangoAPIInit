from rest_framework import serializers
from .models import WDAPI

#class WDAPISerializer(serializers.ModelSerializer):
class WDAPISerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = WDAPI
		fields = ('id', 'url', 'name', 'language', 'price')