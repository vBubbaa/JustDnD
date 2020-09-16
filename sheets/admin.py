from django.contrib import admin
from .models import EmptyCharacterSheet, Feat, CharacterSheetTemplate, TemplateFeat

admin.site.register(EmptyCharacterSheet)
admin.site.register(Feat)
admin.site.register(CharacterSheetTemplate)
admin.site.register(TemplateFeat)
