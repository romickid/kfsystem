"""kfsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^kf_working/', TemplateView.as_view(template_name="kf_working.html")),
    url(r'^customer_newlabel/', TemplateView.as_view(template_name="customer_newlabel.html")),
    url(r'^en_login/', TemplateView.as_view(template_name="en_login.html")),
    url(r'^se_login/', TemplateView.as_view(template_name="se_login.html")),
    url(r'^en_folders/', TemplateView.as_view(template_name="en_folders.html")),
    url(r'^se_folders/', TemplateView.as_view(template_name="se_folders.html")),
    url(r'^se_password_retrieval/', TemplateView.as_view(template_name="se_password_retrieval.html")),
    url(r'^en_password_retrieval/', TemplateView.as_view(template_name="en_password_retrieval.html")),
    url(r'^main/', TemplateView.as_view(template_name="mainpage.html")),
    url(r'^documentation/', TemplateView.as_view(template_name="documentation.html")),
    url(r'^administrator/', TemplateView.as_view(template_name="administrator.html")),
    url(r'^notfound/', TemplateView.as_view(template_name="not_found.html")),
    url(r'^timeout/', TemplateView.as_view(template_name="timeout.html")),
    url(r'^api/', include('backend.urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('backend.urls')),
]
