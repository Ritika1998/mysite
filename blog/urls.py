from django.conf.urls import url, include
from blog.views import home, post_detail, edit_post, del_post, del_com, add_post #view_com

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^(?P<pk>[0-9]+)/$', post_detail, name="post"),
    url(r'^add/$', add_post, name='add_post'),
    url(r'^edit/(?P<pk>[0-9]+)', edit_post, name="edit"),
    #url(r'^view/(?P<id>[0-9]+)', view_com, name = "view"),
    url(r'^(?P<id>[0-9]+)/delete/$', del_post, name="delete_post"),
    url(r'^delcom/(?P<postno>[0-9]+)/(?P<comno>[0-9]+)/$', del_com, name="del_com"),
]
