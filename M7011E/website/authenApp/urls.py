from django.urls import path
from authenApp import views
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.HomePage, name="HomePage"),
    path('SignupPage', views.SignupPage, name="SignupPage"),
    path('LoginPage',views.LoginPage, name="LoginPage"),
    path('SignOut', views.SignOut, name="SignOut"),
    
    #Reset password
    #documentation for how reset password works 
    # https://docs.djangoproject.com/en/4.1/topics/auth/default/
    path('reset_password/',auth_views.PasswordResetView.as_view(), name="reset_password"), #Submit email form
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"), #Email send success message
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"), #link to password for reset
    path('reset_passwordPage_complete/',auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"), #Confirmation that password has been changes.
    
     
    
    

    
  
    
    

    
    
    
]
