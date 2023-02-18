from django.shortcuts import render
from django.views.generic import DeleteView,DetailView,CreateView,ListView,UpdateView
from .models import PostModel
from .form import PostForm,EditForm

# Create your views here.

class HomeBlogView(ListView):
    model=PostModel
    template_name='home.html'

class PostDetailView(DetailView):
    model=PostModel
    template_name='post-detail.html'

class AddPostView(CreateView):
    model=PostModel
    template_name='add-post.html'
    form_class=PostForm

class EditPostView(UpdateView):
    model=PostModel
    template_name='edit-post.html'
    form_class=EditForm
class DeletePostView(DeleteView):
    model=PostModel
    template_name='delete-post.html'
    fields='__all__'
    success_url='/'