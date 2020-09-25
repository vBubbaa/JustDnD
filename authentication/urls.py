from django.urls import path
from rest_framework.authtoken import views
from authentication.views import CustomAuthToken
from authentication import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('obtaintoken/', csrf_exempt(CustomAuthToken.as_view())),
    path('userdata/', views.UserRetrieveUpdateDestroyAPIView.as_view()),
    path('fetchuseroverview/<slug:user>/',
         views.FetchUserOverview.as_view()),
    path('register/', csrf_exempt(views.CreateUser.as_view())),
]
