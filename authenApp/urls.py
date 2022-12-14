from django.urls import path
from authenApp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.HomePage, name="HomePage"),
    path('SignupPage', views.SignupPage, name="SignupPag"),
    path('LoginPage',views.LoginPage, name="LoginPage"),
    path('SignOut', views.SignOut, name="SignOut"),
    path('Profile', views.Profile, name="Profile"),
    path('About', views.About, name="About"),
    path('Contact', views.Contact, name="Contact"),
    path('Back', views.Back, name="Back"),
    path('Leg', views.Leg, name="Leg"),
    path('Chest', views.Chest, name="Chest"),
    path('Arms', views.Arms, name="Arms"),
    path('Shoulder', views.Shoulder, name="Shoulder"),
    path('CalorieCalc', views.CalorieCalc, name="CalorieCalc"),


    #Reset password
    #documentation for how reset password works

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"), #Submit email form

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"), #Email send success message

    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"), #link to password for reset


    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"), #Confirmation that password has been changes.




]
