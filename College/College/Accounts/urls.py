
from django.urls import path
from .views import RegisterUser_view,UserLogin_view,UserLogout_view

urlpatterns = [
    path('reguse/',RegisterUser_view,name='userreg'),
    path('Login/',UserLogin_view,name='LOGIN'),
    path('Logout/',UserLogout_view,name='LOGOUT'),

    
    ]

