from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Blog
class BlogView(CreateView):
    model: Blog

# Create your views here.
