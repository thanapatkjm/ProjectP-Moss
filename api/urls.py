from . import views
from django.urls import path 

urlpatterns = [
    path('get_userdata/',views.get_userdata.as_view()),
    path('update_data/',views.update_data.as_view()),
]
