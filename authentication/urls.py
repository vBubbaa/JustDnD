from django.urls import path
from rest_framework.authtoken import views
from authentication.views import CustomAuthToken

urlpatterns = [
    path('obtaintoken/', CustomAuthToken.as_view())
]
