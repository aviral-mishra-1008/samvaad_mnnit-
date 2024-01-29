from django.urls import path
from . import views
urlpatterns = [
    path("", views.first, name = "firstpost"),
    path('<str:slug>/', views.allpost, name="allpost"),
] 




