from django.contrib import admin
from django.urls import path
from myapp import views
from django.urls import path, include

urlpatterns = [
    path("",views.index,name='home'),
    path("check",views.check,name='check'),
    path("login",views.login,name='login'),
    path("signup",views.signup,name='signup'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
] 