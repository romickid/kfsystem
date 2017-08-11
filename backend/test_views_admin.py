from django.test import TestCase
from django.test import Client
from .views_helper_functions import *
from .views_check_functions import *
from .models import Admin, CustomerService, ChattingLog, SerialNumber, ImageLog, EnterpriseDisplayInfo
from .serializers import AdminSerializer, CustomerServiceSerializer, CustomerServiceCreateSerializer, ChattingLogSerializer, SerialNumberSerializer, EnterpriseDisplayInfoSerializer
import json

class TestAdminCreateCheck(TestCase):
    def setUp(self):
        SerialNumber.objects.create(serials="s1", is_used=False)
        SerialNumber.objects.create(serials="s2", is_used=False)
        SerialNumber.objects.create(serials="s3", is_used=False)
        SerialNumber.objects.create(serials="s4", is_used=True)
        SerialNumber.objects.create(serials="s5", is_used=False)
        SerialNumber.objects.create(serials="s6", is_used=False)
        SerialNumber.objects.create(serials="s7", is_used=False)
        Admin.objects.create(id=1, email="admin1@a.com", nickname="Anick1", password="Apass1", web_url="Aweb_url1", widget_url="Awidget_url1", mobile_url="Amobile_url1", communication_key="Akey1", vid="Avid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email="cs1@a.com", enterprise=admin_instance, nickname="Cnick1", password="Cpass1", is_register=False, is_online=False, connection_num=0, vid="Cvid1")

    def test(self):
        c = Client()
        dict_json1 = {"email": "test1@a.com", "nickname": "nick1", "password": "pass1", "serials": "s1"}
        # a = json.dumps(dict_json1)
        # print(a)
        response1 = c.post("/api/admin_create/", dict_json1)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response1.contexts, "OK")

