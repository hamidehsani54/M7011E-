from django.urls import path
from authenApp import views


urlpatterns = [
    path('', views.HomePage, name="HomePage"),
    
]
