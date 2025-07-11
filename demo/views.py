from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    name = request.GET.get('name', 'Guest')
    return render(request, 'home/home.html', {'name': name})

def greet(request, name):
    return render(request, 'home/home.html', {'name': name})

def api_welcome(request):
    name = request.GET.get('name', 'Guest')
    return JsonResponse({'message': f'Welcome, {name}!'})
