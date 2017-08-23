#coding:utf-8
from django.test import TestCase
from django.test import Client
import sys
sys.path.append("..")
from ..views_helper_functions import *
from ..views_check_functions import *
from ..models import Admin, CustomerService, ChattingLog, SerialNumber, EnterpriseDisplayInfo
from ..serializers import AdminSerializer, CustomerServiceSerializer, CustomerServiceCreateSerializer, ChattingLogSerializer, SerialNumberSerializer, EnterpriseDisplayInfoSerializer
import json


class TestCustomerCheckInfo(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")

    def test(self):
        c = Client()

        json1 = {'enterprise_id': 'a_nick1', 'customer_id': 'customer1', 'cusotmer_name': 'cusotmerName1', 'hash_result': '67e96b8f771e76c253073db39b31782d8ad1bba2d1e7537d596507de5f35bdd92c5d3537f82966af84bef4ada2e2b0c5dc81094132f5ddd0d0c93c3efe978a92'}
        request1 = c.post("/api/customer_check_info/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "True")

        json11 = {'enterprise_id': 'a_nick1', 'customer_id': 'customer1', 'cusotmer_name': 'cusotmerName1', 'hash_result': '41775fd2f10f1d026c9a32d7ea44cad599e6ee53355efd8d4fd834a4e7242c5ad58b98b1aceae836110d5a06b57ad8fc9027905ac97de697fdf87f7ed38b76d1'}
        request11 = c.post("/api/customer_check_info/", data=json.dumps(json11), content_type='json')
        self.assertEqual(request11.status_code, 200)
        self.assertEqual(request11.content.decode('utf-8'), "False")

        json2 = {'enterprise_id': 'a_nick1', 'customer_id': 'customer1', 'cusotmer_name': 'cusotmerName1'}
        request2 = c.post("/api/customer_check_info/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'enterprise_id': 'a_nick1', 'customer_id': 'customer1', 'cusotmer_name': 'cusotmerName1', 'hash_result': 'hash1', 'other': '41775fd2f10f1d026c9a32d7ea44cad599e6ee53355efd8d4fd834a4e7242c5ad58b98b1aceae836110d5a06b57ad8fc9027905ac97de697fdf87f7ed38b76d0'}
        request3 = c.post("/api/customer_check_info/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')


class TestCustomerDisplayCustomerInfoPropertyName(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        instance = Admin.objects.get(id=1)
        EnterpriseDisplayInfo.objects.create(id=1, enterprise=instance, name='id_used', comment='this is id')
        EnterpriseDisplayInfo.objects.create(id=2, enterprise=instance, name='id_used1', comment='this is id2')

    def test(self):
        c = Client()

        json1 = {'enterprise_id': 'a_nick1'}
        request1 = c.post("/api/customer_display_customerinfopropertyname/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        # print(request1.content.decode('utf-8'))

        json2 = {}
        request2 = c.post("/api/customer_display_customerinfopropertyname/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'enterprise_id': 'a_nick1', 'other': 'other'}
        request3 = c.post("/api/customer_display_customerinfopropertyname/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')
