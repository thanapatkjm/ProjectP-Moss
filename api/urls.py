from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('get_userdata/',views.get_userdata.as_view()),
    path('update_data/',views.update_data.as_view()),
]
