from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'advito/index.html')


def about(request):
    return render(request, 'advito/about.html')


def support(request):
    return render(request, 'advito/Support.html')


def create_ad(request):
    return render(request, 'advito/Support.html')


def edit_ad(request):
    return render(request, 'advito/Support.html')


def delete_ad(request):
    return render(request, 'advito/Support.html')


def add_to_favor(request):
    return render(request, 'advito/Support.html')


def view_ad_detail(request):
    return render(request, 'advito/Support.html')
