from rest_framework import serializers
from . import models


class FeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feat
        fields = ['featName', 'featVal']


class EmptyCharacterSheetSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    charactersheetfeat = FeatSerializer(many=True, required=False)

    class Meta:
        model = models.EmptyCharacterSheet
        fields = '__all__'

    # Handle feat creation for sheet
    def create(self, validated_data):
        feat_data = validated_data.pop('charactersheetfeat')
        print(str(feat_data))
        sheet = models.EmptyCharacterSheet.objects.create(**validated_data)
        for feat in feat_data:
            models.Feat.objects.create(characterSheet=sheet, **feat)
        return sheet

# {
#     "charactersheetfeat": [
#          {
#                 "featName": "str",
#                 "featVal": "32"
#             }
#     ],
#     "name": "feattest",
#     "slug": "",
#     "bio": "",
#     "hp": null
# }
