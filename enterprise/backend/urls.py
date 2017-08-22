from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/admin_create/$', views.admin_create),
    url(r'^api/admin_login/$', views.admin_login),
    url(r'^api/admin_reset_password/$', views.admin_reset_password),
    url(r'^api/admin_forget_password_email_request/$', views.admin_forget_password_email_request),
    url(r'^api/admin_show_communication_key/$', views.admin_show_communication_key),
    url(r'^api/admin_forget_password_email_request/$', views.admin_forget_password_email_request),
    url(r'^api/admin_forget_password_save_data/', views.admin_forget_password_save_data),
    url(r'^api/admin_show_user_status/', views.admin_show_user_status),
    url(r'^api/admin_send_info/', views.admin_send_info),
    url(r'^api/admin_logout/', views.admin_logout),
    url(r'^api/admin_get_info/', views.admin_get_info),
    url(r'^api/admin_get_info_iframe/', views.admin_get_info_iframe),

]
