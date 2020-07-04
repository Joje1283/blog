from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from tagging.views import TaggedObjectList
from .models import Post


def home_view(request):
    paginate_by = 15
    query = request.GET.get('q')
    page = request.GET.get('page', 1)
    posts = Post.objects.all()
    if query:
        posts = posts.filter(Q(subject__icontains=query) | Q(content__icontains=query))
    paginator = Paginator(posts, paginate_by)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

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
    paginate_by = 15