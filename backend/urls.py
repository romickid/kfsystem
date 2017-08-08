from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/admin_create/$', views.admin_create),
    url(r'^api/admin_login/$', views.admin_login),
    url(r'^api/admin_reset_password/$', views.admin_reset_password),
    url(r'^api/admin_find_password_email_request/$', views.admin_find_password_email_request),   
    url(r'^api/admin_show_communication_key/$', views.admin_show_communication_key),
    url(r'^api/admin_reset_communication_key/$', views.admin_reset_communication_key),
    url(r'^api/admin_find_password_email_request/$', views.admin_find_password_email_request),
    url(r'^api/admin_find_password_check_vid/', views.admin_find_password_check_vid),

    url(r'^api/customerservice_create/$', views.customerservice_create),
    url(r'^api/customerservice_set_profile/$', views.customerservice_set_profile),
    url(r'^api/customerservice_login/$', views.customerservice_login),
    url(r'^api/customerservice_reset_password/$', views.customerservice_reset_password),
    url(r'^api/customerservice_find_password_email_request/$', views.customerservice_find_password_email_request),
    url(r'^api/customerservice_find_check_vid/', views.customerservice_find_password_check_vid),
    url(r'^api/customerservice_show_status/', views.customerservice_show_status),

    url(r'^api/chattinglog_send_message/$', views.chattinglog_send_message),
    url(r'^api/chattinglog_get_data/$', views.chattinglog_get_data),
    url(r'^api/chattinglog_delete_record/$', views.chattinglog_delete_record),
    url(r'^api/chattinglog_delete_record_ontime/$', views.chattinglog_delete_record_ontime),
    url(r'^api/chattinglog_status_change/$', views.chattinglog_status_change),
]
