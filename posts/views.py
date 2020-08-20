from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from .models import post

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def post_detail_view(request, post_id, *args, **kwargs):
    
    data = {
        'id' : post_id
    } 
    try:
        obj = post.objects.get(id=post_id)
        data['content'] = obj.content
        # data['image_path'] = obj.image.url
        status = 200
    except:
        data['message'] = 'Object Not Found'
        status = 404
    
    return JsonResponse(data,status=status)