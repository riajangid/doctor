from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_viewer,name='login_viewer'),
    path('registration_viewer',views.registration_viewer,name='registration_viewer'),
    path('index_viewer',views.index_viewer,name='index_viewer'),
        
]
    


    
