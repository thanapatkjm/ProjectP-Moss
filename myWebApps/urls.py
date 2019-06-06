from django.urls import path 
from . import views
from django.views.generic import TemplateView

app_name = 'myWeb'
urlpatterns = [
    path('',views.home, name='home'),
    path('authenUser/',views.authenUser, name='authenUser'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('changepass/',views.changepass,name='changepass'),
    path('passChanged/',views.passChanged,name='passChanged'),
    path('adminHome/',views.adminHome,name='adminHome'),
    path('userPage/id=<int:user_id>',views.userPage,name='userPage'),
    path('home_package/',views.adminHome_package,name='home_package'),
    path('package_action/<int:package_id>',views.package_action, name='package_action'),
    path('new_package/',views.new_package,name="new_package"),
    path('delete_log/<int:id>',views.delete_log,name="delete_log"),
    path('expense/<int:user_id>',views.expense, name="expense"),
]
