from django.urls import path
from . import views

urlpatterns = [
    path('charactersheet/create/', views.EmptyCharacterSheetCreate.as_view()),
    path('charactersheet/list/', views.EmptyCharacterSheetList.as_view()),
    path('charactersheet/<int:pk>/', views.EmptyCharacterSheetGetUpdate.as_view()),
    path('charactersheet/<int:pk>/delete/',
         views.EmptyCharacterSheetDelete.as_view()),
]
