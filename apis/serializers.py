from rest_framework import serializers

from vino.models import Vino

class VinoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vino
        fields='__all__'
