from django.shortcuts import render, get_object_or_404
from .models import Post


def home_view(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
    })


def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {
        'post': post,
    })


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    return render(request, 'about.html')


def sample_post_view(request):
    return render(request, 'sample.html')
