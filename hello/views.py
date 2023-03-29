import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting, Producto

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def db(request):

    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def user(request):
    producto=Producto()
    producto.save()
    productos = Producto.objects.all()
    
    return render(request, "user.html", {"productos": productos})

def driver(request):
    producto=Producto.objects.last()
    return render(request, "driver.html",{"producto": producto} )

def provider(request):
    if request.method == 'POST':
        if request.POST.get('category') and request.POST.get('title') and  request.POST.get('price') and request.POST.get('minimal'):
                producto=Producto()
                producto.category = request.POST.get('category')
                producto.title = request.POST.get('title')
                producto.price = request.POST.get('price')
                producto.minimal = request.POST.get('minimal')
                producto.save()
    productos = Producto.objects.all()
    return render(request, "provider.html", {"productos": productos})

