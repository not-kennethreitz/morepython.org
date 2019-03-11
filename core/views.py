from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    paginate_by = 50

    def get_queryset():
        Post.objects.filter(published=True)

    def get(self, request, *args, **kwargs):
        return render(request, template_name="index.html")


# Create your views here.
class PostDetailView(DetailView):
    model = Post

    def get_queryset():
        Post.objects.filter(published=True)

    def get(self, request, *args, **kwargs):
        return render(request, template_name="index.html")
