from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    model = Article
    template_name = 'hello/index.html'
