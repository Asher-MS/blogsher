from django.shortcuts import render,redirect
from .models import Article,Sample
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def articleslist(req):
    if(req.method=="POST"):
        print(req)
        
    else:
        articles=Article.objects.all().order_by("date")
        samples=Sample.objects.all()
        return render(req,"articles/articlelist.html",{'articles':articles})

def article_detail(req,slug):
    for i in Article.objects.all():
        if(i.slug==slug):
            return render(req,"articles/article.html",{"article":i})
            


@login_required(login_url="/accounts/login/")
def article_create(req):
    if(req.method=="POST"):
        form=forms.CreateArticle(req.POST,req.FILES)
        if(form.is_valid):
            #Save this to the Database
            article=Article()
            article=form
            article.save()
            return(redirect("articles:list"))

    else:
        form=forms.CreateArticle()
    return render(req,"articles/create.html",{"form":form})