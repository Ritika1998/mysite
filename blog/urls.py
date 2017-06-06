from django.conf.urls import url

from blog import views
from blog.views import home, view_post

urlpatterns = [

    url('^$', home, name="home"),
    url(r'^(?P<id>[0-9]+)/$', view_post, name = "post"),
]