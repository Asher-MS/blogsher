from django.shortcuts import render
from .models import Article,Sample
from django.http import HttpResponse
# Create your views here.

def articleslist(req):
    articles=Article.objects.all().order_by("date")
    samples=Sample.objects.all()
    return render(req,"articles/articlelist.html",{'articles':articles})

def article_detail(req,slug):
    for i in Article.objects.all():
        if(i.slug==slug):
            return render(req,"articles/article.html",{"article":i})
            
    