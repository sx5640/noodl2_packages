from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from .models import *

# Create your views here.
def source_detail(request, source_title):
    source = get_object_or_404(Source, title = source_title)
    articles = source.article_set.order_by("-publication_time")[:30]
    context = {"source": source, "articles": articles}   
    return render(request, "source/detail.html", context)

def article_detail(request, source_title, article_id):
    context = {"article": get_object_or_404(Article, id = article_id)} 
    return render(request, "article/detail.html", context)        
        
        


