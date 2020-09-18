from rest_framework import generics
from rest_framework.response import Response
from .serializers import EmptyCharacterSheetSerializer, TemplateSerializer
from .models import EmptyCharacterSheet, CharacterSheetTemplate
from sheets.permissions import IsOwnerOrReadOnly
from sheets.pagination import StandardPagination


# # # # # # # # # # # # Character Sheets # # # # # # # # # # # #

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
        user = self.kwargs['slug']
        return EmptyCharacterSheet.objects.filter(user__username=user)


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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # Templates # # # # # # # # # # # # # # # #

# Create template view
class TemplateCreate(generics.CreateAPIView):
    queryset = CharacterSheetTemplate.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# List template view for all templates in the DB
class TemplateList(generics.ListAPIView):
    queryset = CharacterSheetTemplate.objects.all()
    serializer_class = TemplateSerializer
    pagination_class = StandardPagination


# Character sheet list view by user
class TemplateUserList(generics.ListAPIView):
    queryset = CharacterSheetTemplate.objects.all()
    serializer_class = TemplateSerializer

    def get_queryset(self):
        user = self.kwargs['slug']
        return CharacterSheetTemplate.objects.filter(user__username=user)


# Retrieve/update sheet view
class TemplateGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = CharacterSheetTemplate.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [IsOwnerOrReadOnly]


# Delete sheet view
class TemplateDelete(generics.DestroyAPIView):
    queryset = CharacterSheetTemplate.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [IsOwnerOrReadOnly]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
