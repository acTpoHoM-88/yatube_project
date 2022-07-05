from django.shortcuts import render

# Create your views here.
# post/views.py
from django.http import HttpResponse

# Главная страница
def index(request):    
    return HttpResponse('Main page')


# Страница группы
def group_posts(request, slug):
    return HttpResponse(f' Group {slug} page')