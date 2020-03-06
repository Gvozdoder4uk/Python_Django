from django.shortcuts import render, render_to_response
from .models import Visual


# Create your views here.

def index(request):
    return render(request, 'htmls_ECP/homePage.html')


def login(request):
    return render(request, 'htmls_ECP/login_Page.html')


def contact(request):
    return render(request, 'htmls_ECP/contact_form.html',
                  {'values': ['Если у вас остались вопросы задайте их по телефону','8(925)321-75-68','fokin_ok@rusagrotrans.ru']})


def vision(request):
    visuals = Visual.objects.order_by('index').all()
    return render_to_response('vision.html', {'visuals': visuals})