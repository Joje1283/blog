from django.http import HttpResponse
import json
from posts.models import Contact


def contact(request):
    if request.method == 'POST':
        data = {'name': request.POST.get('name'), 'phone': request.POST.get('phone'),
                'email': request.POST.get('email'), 'message': request.POST.get('message')}
        Contact.objects.create(**data)
        return HttpResponse(json.dumps(data), content_type="application/json")