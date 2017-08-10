from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/admin_create/$', views.admin_create),
    url(r'^api/admin_login/$', views.admin_login),
    url(r'^api/admin_reset_password/$', views.admin_reset_password),
    url(r'^api/admin_forget_password_email_request/$', views.admin_forget_password_email_request),
    url(r'^api/admin_show_communication_key/$', views.admin_show_communication_key),
    url(r'^api/admin_reset_communication_key/$', views.admin_reset_communication_key),
    url(r'^api/admin_forget_password_email_request/$', views.admin_forget_password_email_request),
    url(r'^api/admin_forget_password_check_vid/', views.admin_forget_password_check_vid),
    url(r'^api/admin_forget_password_save_data/', views.admin_forget_password_save_data),
    url(r'^api/admin_show_cs_status/', views.admin_show_cs_status),
    url(r'^api/admin_show_user_status/', views.admin_show_user_status),
    url(r'^api/admin_display_info_create/', views.admin_display_info_create),
    url(r'^api/admin_display_info_delete/', views.admin_display_info_delete),
    url(r'^api/admin_logout/', views.admin_logout),

    url(r'^api/customerservice_create/$', views.customerservice_create),
    url(r'^api/customerservice_set_profile/$', views.customerservice_set_profile),
    url(r'^api/customerservice_set_profile_check_vid/$', views.customerservice_set_profile_check_vid),
    url(r'^api/customerservice_login/$', views.customerservice_login),
    url(r'^api/customerservice_reset_password/$', views.customerservice_reset_password),
    url(r'^api/customerservice_forget_password_email_request/$', views.customerservice_forget_password_email_request),
    url(r'^api/customerservice_forget_password_check_vid/', views.customerservice_forget_password_check_vid),
    url(r'^api/customerservice_forget_password_save_data/', views.customerservice_forget_password_save_data),
    url(r'^api/customerservice_show_user_status/', views.customerservice_show_user_status),
    url(r'^api/customerservice_logout/', views.customerservice_logout),

    url(r'^api/chattinglog_send_message/$', views.chattinglog_send_message),
    url(r'^api/chattinglog_get_data/$', views.chattinglog_get_data),
    url(r'^api/chattinglog_delete_record/$', views.chattinglog_delete_record),
    url(r'^api/chattinglog_delete_record_ontime/$', views.chattinglog_delete_record_ontime),
    url(r'^api/chattinglog_status_change/$', views.chattinglog_status_change),
]
