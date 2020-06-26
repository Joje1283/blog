from django.shortcuts import render, get_object_or_404
from tagging.views import TaggedObjectList
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


def tag_view(request):
    return render(request, 'tagging_cloud.html')


class PostTaggedObjectList(TaggedObjectList):
    model = Post
    template_name = 'tagging_post_list.html'

