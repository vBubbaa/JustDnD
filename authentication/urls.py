from django.urls import path
from rest_framework.authtoken import views
from authentication.views import CustomAuthToken
from authentication import views

urlpatterns = [
    path('obtaintoken/', CustomAuthToken.as_view()),
    path('userdata/', views.UserRetrieveUpdateDestroyAPIView.as_view()),
]
