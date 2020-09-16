from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'advito/index.html')


def about(request):
    return render(request, 'advito/about.html')


def support(request):
    return render(request, 'advito/Support.html')