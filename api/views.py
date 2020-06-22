from django.http import HttpResponse
import json

# Create your views here.
def contact(request):
    # pk = request.POST.get('pk', None)  # ajax 통신을 통해서 template에서 POST방식으로 전달
    # post = get_object_or_404(Post, pk=pk)
    # post_like, post_like_created = post.like_set.get_or_create(user=request.user)
    #
    # if not post_like_created:
    #     post_like.delete()
    #     message = "좋아요 취소"
    # else:
    #     message = "좋아요"

    context = {'name': 1,
               'phone': 2,
               'email': 3,
               'message': 4}

    return HttpResponse(json.dumps(context), content_type="application/json")