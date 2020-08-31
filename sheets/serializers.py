from rest_framework import serializers
from . import models


class EmptyCharacterSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmptyCharacterSheet
        fields = '__all__'
