from django.shortcuts import render
from django.contrib import auth
from django.template import RequestContext


# Create your views here.

def index(request):
    return render(request, 'htmls_ECP/homePage.html')



def contact(request):
    return render(request, 'htmls_ECP/contact_form.html',
                  {'values': ['Если у вас остались вопросы задайте их по телефону', '8(925)321-75-68',
                              'fokin_ok@rusagrotrans.ru']})

