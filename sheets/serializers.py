from rest_framework import serializers
from . import models


class FeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feat
        fields = ['featName', 'featVal', 'pk']


class EmptyCharacterSheetSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    charactersheetfeat = FeatSerializer(many=True, required=False)

    class Meta:
        model = models.EmptyCharacterSheet
        fields = '__all__'

    # Handle feat creation for sheet
    def create(self, validated_data):
        feat_data = validated_data.pop('charactersheetfeat')
        sheet = models.EmptyCharacterSheet.objects.create(**validated_data)
        for feat in feat_data:
            models.Feat.objects.create(characterSheet=sheet, **feat)
        return sheet

    def update(self, instance, validated_data):
        # Response data
        feat_data = validated_data.pop('charactersheetfeat')
        # DB Data
        feats = dict((i.id, i) for i in instance.charactersheetfeat.all())
        print(str(feats))

        instance.name = validated_data.get('name', instance.name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.hp = validated_data.get('hp', instance.hp)
        instance.save()

        for feat in feat_data:
            if 'id' in feat:
                f = feats.pop(feat['id'])
                f.featName = feat['featName']
                f.featVal = feat['featVal']
                f.save()

            else:
                models.Feat.objects.create(characterSheet=instance, **feat)

        if len(feats) > 0:
            for feat in feats.values():
                feat.delete()
        return instance


class TemplateFeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TemplateFeat
        fields = ['featName', 'featVal', 'pk']


class TemplateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    templatefeat = TemplateFeatSerializer(many=True, required=False)

    class Meta:
        model = models.CharacterSheetTemplate
        fields = '__all__'

    # Handle feat creation for sheet
    def create(self, validated_data):
        feat_data = validated_data.pop('templatefeat')
        template = models.CharacterSheetTemplate.objects.create(
            **validated_data)
        for feat in feat_data:
            models.TemplateFeat.objects.create(template=template, **feat)
        return template

    def update(self, instance, validated_data):
        # Response data
        feat_data = validated_data.pop('templatefeat')
        # DB Data
        feats = dict((i.id, i) for i in instance.templatefeat.all())

        instance.oneshot = validated_data.get('oneshot', instance.oneshot)
        instance.oneshoturl = validated_data.get(
            'oneshoturl', instance.oneshoturl)
        instance.save()

        for feat in feat_data:
            if 'id' in feat:
                f = feats.pop(feat['id'])
                f.featName = feat['featName']
                f.featVal = feat['featVal']
                f.save()

            else:
                models.TemplateFeat.objects.create(template=instance, **feat)

        if len(feats) > 0:
            for feat in feats.values():
                feat.delete()
        return instance
