from django.shortcuts import render
from django.http import HttpResponse
from item.models import Category, Item
# This is a request handler
# create view functions here
# view function takes a request and sends a response to that

def say_hello(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'hello.html', {
            'categories': categories,
            'items': items,
            'name': 'AK',
        })

def contact(request):
    return render(request, 'contact.html')