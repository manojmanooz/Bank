
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.signup,name="signup"),
    path('Login/',views.login,name="login"),
    path('form/',views.form,name="form"),
    path('welcome/',views.welcome,name="welcome"),
    path('logout/',views.logout,name='logout'),
]
