from rest_framework import generics
from rest_framework.response import Response
from .serializers import EmptyCharacterSheetSerializer
from .models import EmptyCharacterSheet
from sheets.permissions import IsOwnerOrReadOnly


# Create character sheet view
class EmptyCharacterSheetCreate(generics.CreateAPIView):
    queryset = EmptyCharacterSheet.objects.all()
    serializer_class = EmptyCharacterSheetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# List character sheet view for all character sheets in the DB
class EmptyCharacterSheetList(generics.ListAPIView):
    queryset = EmptyCharacterSheet.objects.all()
    serializer_class = EmptyCharacterSheetSerializer


# Character sheet list view by user
class EmptyCharacterSheetUserList(generics.ListAPIView):
    queryset = EmptyCharacterSheet.objects.all()
    serializer_class = EmptyCharacterSheetSerializer

    def get_queryset(self):
        user = self.kwargs['pk']
        return EmptyCharacterSheet.objects.filter(user__id=user)


# Retrieve/update sheet view
class EmptyCharacterSheetGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = EmptyCharacterSheet.objects.all()
    serializer_class = EmptyCharacterSheetSerializer
    permission_classes = [IsOwnerOrReadOnly]


# Delete sheet view
class EmptyCharacterSheetDelete(generics.DestroyAPIView):
    queryset = EmptyCharacterSheet.objects.all()
    serializer_class = EmptyCharacterSheetSerializer
    permission_classes = [IsOwnerOrReadOnly]
