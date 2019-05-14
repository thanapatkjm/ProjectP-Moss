from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('get_user/',views.get_user.as_view()),
]
