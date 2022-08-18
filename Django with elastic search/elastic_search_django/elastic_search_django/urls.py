from operator import imod
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from search.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', home),
    path('generate/', index),
    path('searchpost/' , search, name = "search"),
    path('multimatch/' , multimatch, name = "multimatch"),
    path('delete/<int:pk>/' , delete, name = "delete"),
    path('viewposts/' , viewposts, name = "viewposts"),
    # path('search/' , PublisherDocumentView.as_view({'get': 'list'})),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)