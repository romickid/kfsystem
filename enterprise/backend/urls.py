from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/customer_create/$', views.customer_create),
    url(r'^api/customer_login/$', views.customer_login),
    url(r'^api/customer_show_user_info/$', views.customer_show_user_info),
    url(r'^api/customer_show_user_login_status/$', views.customer_show_user_login_status),
    url(r'^api/customer_logout/$', views.customer_logout),
    url(r'^api/communication_key_update/$', views.communication_key_update),
    url(r'^api/customer_get_web_url/', views.customer_get_web_url),
    url(r'^api/customer_get_widget_url/', views.customer_get_widget_url),
    url(r'^api/customer_get_mobile_url/', views.customer_get_mobile_url),
]
