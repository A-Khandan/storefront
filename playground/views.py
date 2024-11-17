from django.shortcuts import render
from django.http import HttpResponse
# This is a request handler
# create view functions here
# view function takes a request and sends a response to that

def say_hello(request):
    return render(request, 'hello.html', {'name': 'AK'})