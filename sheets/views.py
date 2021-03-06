from rest_framework import generics
from rest_framework.response import Response
from .serializers import EmptyCharacterSheetSerializer, TemplateSerializer
from .models import EmptyCharacterSheet, CharacterSheetTemplate
from sheets.permissions import IsOwnerOrReadOnly
from sheets.pagination import StandardPagination
from rest_framework import filters
from rest_framework import status
from sheets.Exceptions import CharacterSheetLimitExceeded, TemplateLimitExceeded


# # # # # # # # # # # # Character Sheets # # # # # # # # # # # #

# Create character sheet view
class EmptyCharacterSheetCreate(generics.CreateAPIView):
    queryset = EmptyCharacterSheet.objects.all()
    serializer_class = EmptyCharacterSheetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Limit users to only 10 character sheets
        if (EmptyCharacterSheet.objects.filter(
                user=self.request.user).count() < 10 or self.request.user.verified):
            serializer.save(user=self.request.user)
        else:
            raise CharacterSheetLimitExceeded()


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
        # Limit users to only 10 character sheets
        if (CharacterSheetTemplate.objects.filter(
                user=self.request.user).count() < 10 or self.request.user.verified):
            serializer.save(user=self.request.user)
        else:
            raise TemplateLimitExceeded()


# List template view for all templates in the DB
class TemplateList(generics.ListAPIView):
    queryset = CharacterSheetTemplate.objects.all()
    serializer_class = TemplateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['oneshot', 'user__username', 'oneshoturl']
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
