from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from .models import EP_Keys

urlpatterns = [
    url(r'^$',views.requests_access),
    url(r'keys/$', ListView.as_view(queryset=EP_Keys.objects.all().order_by("date_expired"),
                                template_name="access_app/EP.html")),
    url(r'account/', views.access_req)

]
