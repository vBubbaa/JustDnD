from rest_framework import generics
from rest_framework.response import Response
from .serializers import EmptyCharacterSheetSerializer
from .models import EmptyCharacterSheet


# Create character sheet view
class EmptyCharacterSheetCreate(generics.CreateAPIView):
    queryset = EmptyCharacterSheet.objects.all()
    serializer_class = EmptyCharacterSheetSerializer


# List character sheet view
class EmptyCharacterSheetList(generics.ListAPIView):
    queryset = EmptyCharacterSheet.objects.all()
    serializer_class = EmptyCharacterSheetSerializer


# Retrieve/update sheet view
class EmptyCharacterSheetGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = EmptyCharacterSheet.objects.all()
    serializer_class = EmptyCharacterSheetSerializer


# Delete sheet view
class EmptyCharacterSheetDelete(generics.DestroyAPIView):
    queryset = EmptyCharacterSheet.objects.all()
    serializer_class = EmptyCharacterSheetSerializer
