from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from .models import Articles,EP_Keys

urlpatterns = [
    url(r'news$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
                                template_name="access_news/posts.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles, template_name="access_news/news.html")),
    url(r'$', ListView.as_view(queryset=EP_Keys.objects.all().order_by("date_expired"),
                                template_name="access_news/EP.html")),

]
