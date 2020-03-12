from django.shortcuts import render
import openpyxl


# Create your views here.
def access_req(request):
    return render(request, 'access_app/EP_account.html')


def requests_access(request):
    return render(request, 'access_app/Request.html')

