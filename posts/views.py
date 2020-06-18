from django.shortcuts import render, get_object_or_404

from posts.models import Post


def home_view(request):
    return render(request, 'index.html')


def post_view(request, pk):
    # post = get_object_or_404(Post, pk)
    post = Post.objects.filter(pk=pk).first()
    return render(request, 'post.html', {
        'post': post
    })
