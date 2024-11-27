from django.urls import path #importing the path module for sorting out urls
from . import views  #from current folder import views module

app_name = 'playground'

#URL config
urlpatterns = [
    path('', views.say_hello, name = "hello"),
    path("contact/", views.contact, name = "contact"),
    path("signup/", views.signup, name = "signup")
]
