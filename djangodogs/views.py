from django.shortcuts import render
from .models import Dog
from django.http import Http404


def home(request):
    dogs = Dog.objects.all()
    return render(request, 'home.html', {'dogs': dogs})


def dog_detail(request, id):
    dog = Dog.objects.get(id=id)
    return render(request, 'dog_detail.html', {'dog': dog})
