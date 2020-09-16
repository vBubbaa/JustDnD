from django.urls import path
from . import views

urlpatterns = [
    # Character sheet views
    path('charactersheet/create/', views.EmptyCharacterSheetCreate.as_view()),
    path('charactersheet/list/', views.EmptyCharacterSheetList.as_view()),
    path('charactersheetuser/list/<slug:slug>/',
         views.EmptyCharacterSheetUserList.as_view()),
    path('charactersheet/<int:pk>/', views.EmptyCharacterSheetGetUpdate.as_view()),
    path('charactersheet/<int:pk>/delete/',
         views.EmptyCharacterSheetDelete.as_view()),
    # Template views
    path('template/create/', views.TemplateCreate.as_view()),
    path('template/list/', views.TemplateList.as_view()),
    path('template/list/<slug:slug>/',
         views.TemplateUserList.as_view()),
    path('template/<int:pk>/', views.TemplateGetUpdate.as_view()),
    path('template/<int:pk>/delete/',
         views.TemplateDelete.as_view()),
]
