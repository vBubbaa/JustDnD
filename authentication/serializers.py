from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator


# User serializer
class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'bio', 'pk', 'verified']
        read_only_fields = ['verified']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
