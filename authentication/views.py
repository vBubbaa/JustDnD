from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics, permissions
from sheets import permissions
from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': {
                'user_id': user.pk,
                'username': user.username,
            }
        })


# User get, put, delete
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.IsOwnerOrReadOnly,)

    def get_object(self):
        return self.request.user


class FetchUserOverview(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_object(self):
        try:
            return CustomUser.objects.get(username=self.kwargs['user'])
        except CustomUser.DoesNotExist:
            raise Http404


# Create user (Register)
class CreateUser(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
