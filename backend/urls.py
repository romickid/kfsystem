from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/admin_create/$', views.admin_create),
    url(r'^api/admin_set_profile/$', views.admin_set_profile),
    url(r'^api/admin_login/$', views.admin_login),
    url(r'^api/admin_reset_password/$', views.admin_reset_password),
    url(r'^api/customerservice_create/$', views.customerservice_create),
    url(r'^api/customerservice_set_profile/$', views.customerservice_set_profile),
    url(r'^api/customerservice_login/$', views.customerservice_login),
    url(r'^api/customerservice_reset_password/$', views.customerservice_reset_password),
    url(r'^api/chattinglog_send_message/$', views.chattinglog_send_message),
    url(r'^api/(?P<pk>[0-9]+)/$', views.chattinglog_get_data),
    url(r'^api/chattinglog_delete_record/$', views.chattinglog_delete_record),
    
]
