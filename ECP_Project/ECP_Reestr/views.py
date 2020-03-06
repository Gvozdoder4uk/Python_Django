from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'htmls_ECP/homePage.html')

def login(request):
    return render(request, 'htmls_ECP/login_Page.html')
