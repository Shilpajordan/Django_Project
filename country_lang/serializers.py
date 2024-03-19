from rest_framework import serializers
from .models import Countries


# model Serializer
class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = "__all__"