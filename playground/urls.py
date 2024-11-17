from django.urls import path #importing the path module for sorting out urls
from . import views  #from current folder import views module


#URL config
urlpatterns = [
    path('hello/', views.say_hello)
]
