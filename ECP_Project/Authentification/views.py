from django.shortcuts import render
from django.contrib import auth
from django.template import RequestContext

# Create your views here.

def login(request):
    return render(request, 'loginapp/login_Page.html')