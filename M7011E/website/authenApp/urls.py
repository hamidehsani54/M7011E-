from django.urls import path
from authenApp import views



urlpatterns = [
    path('', views.HomePage, name="HomePage"),
    path('SignupPage', views.SignupPage, name="SignupPage"),
    path('LoginPage',views.LoginPage, name="LoginPage"),
    path('ResetPasswordPage', views.ResetPasswordPage, name="ResetPasswordPage"),
    path('SignOut', views.SignOut, name="SignOut"),
    

    
  
    
    

    
    
    
]
