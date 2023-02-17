from django.shortcuts import render
from django.views.generic import DeleteView,DetailView,CreateView,ListView
from .models import PostModel

# Create your views here.

class HomeBlogView(ListView):
    model=PostModel
    template_name='home.html'
