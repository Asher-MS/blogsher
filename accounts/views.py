from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup(req):
    form=UserCreationForm()
    return render(req,"accounts/signup.html",{'form':form})