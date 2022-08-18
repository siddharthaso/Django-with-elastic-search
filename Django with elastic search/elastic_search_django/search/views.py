from django.shortcuts import render,redirect

from django.http import JsonResponse
import requests
import json
from search.models import *

from .documents import *
# from .serializers import *

# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     CompoundSearchFilterBackend
# )
# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     OrderingFilterBackend,
# )

# Create your views here.
def home(request):
    return render(request,'html/home.html')

def viewposts(request):
    posts = ElasticDemo.objects.all()
    return render(request, 'search/search.html',{'posts':posts})

def generate_random_data():
    url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=3dcc0aaee8cb4d2cbbfa36a0fb3eb4a7'
    r = requests.get(url)
    payload = json.loads(r.text)
    count = 1
    for data in payload.get('articles'):
        print(count)
        if data.get('description')!=None:
            ElasticDemo.objects.create(
                title = data.get('title'),
                content = data.get('description')
            )
            count +=1

def index(request):
    generate_random_data()
    return JsonResponse({'status' : 200})


# class PublisherDocumentView(DocumentViewSet):
#     document = News1Document
#     # serializer_class = NewsDocumentSerializer
#     lookup_field = 'first_name'
#     fielddata=True
#     # filter_backends = [
#     #     FilteringFilterBackend,
#     #     OrderingFilterBackend,
#     #     CompoundSearchFilterBackend,
#     # ]
   
#     search_fields = (
#         'title',
#         'content',
#     )
#     multi_match_search_fields = (
#        'title',
#         'content',
#     )
#     filter_fields = {
#        'title' : 'title',
#         'content' : 'content',
#     }
#     ordering_fields = {
#         'id': None,
#     }
#     ordering = ( 'id'  ,)
        
def search(request):
    q = request.GET.get('q')
    if q:
        posts = News1Document.search().query("match",title =q)
        # s = Search(index='i').query("match", title="python")
    else:
        posts = ''
    return render(request, 'search/search.html',{'posts':posts})

def delete(request,pk):
    # for delete
    posts = News1Document.search().query("match",id =pk)
    response = posts.delete()
    return redirect('viewposts')
    
# from elasticsearch_dsl import Q
def multimatch(request):
    q = request.GET.get('q')
    if q:
        posts = News1Document.search().query("multi_match", query=q, fields=['title', 'content'])
    else:
        posts = ''
    return render(request, 'search/search.html',{'posts':posts})
