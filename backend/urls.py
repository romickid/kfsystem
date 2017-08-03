from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/$', views.snippet_list),
    url(r'^api/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^api/admin_create/$', views.admin_create),
    url(r'^api/admin_set_profile/$', views.admin_set_profile),
    url(r'^api/admin_login/$', views.admin_login),
    url(r'^api/admin_reset_password/$', views.admin_reset_password),
]
