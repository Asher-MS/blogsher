from django.http import HttpResponse
from django.shortcuts import render


def about(req):
    # return HttpResponse("<h1>This Is an nice webpage<h1> ")
    return render(req,"about.html")

def homepage(req):
    return render(req,"homepage.html")
    # return HttpResponse("<h1>This is the Homepage</h1>")

    
