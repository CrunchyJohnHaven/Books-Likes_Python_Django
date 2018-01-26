from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^logout$', views.logout),
    url(r'^success$', views.success),
    url(r'^register/$', views.register),
    url(r'^belt/$', views.belt),
    url(r'^books/$', views.books),
    url(r'^add$', views.add),
    url(r'^books/\d$', views.oneBook),
    url(r'^users/\d$', views.oneUser),
]