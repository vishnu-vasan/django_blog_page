from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'articles'

# namespacing to avoid conflict with other apps
urlpatterns = [
    url(r'^$',views.article_list,name="list"),
    url(r'^create/$',views.article_create,name='create'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail,name="detail"),
]
