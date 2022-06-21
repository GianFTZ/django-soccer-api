from rest_framework import serializers
from sports.models import Local

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ['nome', 'price']
        