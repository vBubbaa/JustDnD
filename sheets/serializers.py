from rest_framework import serializers
from . import models


class EmptyCharacterSheetSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = models.EmptyCharacterSheet
        fields = '__all__'
