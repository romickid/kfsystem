from django.test import TestCase
import json
from ..models import ChattingLog, Admin, CustomerService
from django.test.client import Client


class Test_chattinglog_send_message(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

    def test(self):
        c = Client()
        json1 = {'client_id': '1','service_id': '1','content': 'hahaha','is_client': 1,'time': '2017-08-11 13:33:33'}
        response = c.post('/api/chattinglog_send_message/', data=json.dumps(json1), content_type='json')
        self.assertEqual(response.status_code, 200)
        json2 = {'client_id': '2','service_id': '1','content': 'sdfr','is_client': 0,'time': '2017-08-03 10:12:33'}
        response = c.post('/api/chattinglog_send_message/', data=json.dumps(json2), content_type='json')
        self.assertEqual(response.status_code, 200)
        json3 = {'client_id': '3','service_id': '2','content': 'iuewr','is_client': 1,'time': '2017-08-10 09:33:33'}
        response = c.post('/api/chattinglog_send_message/', data=json.dumps(json3), content_type='json')
        self.assertEqual(response.status_code, 201)
        json4 = {'client_id': '4','service_id': '8','content': 'uyv','is_client': 0,'time': '2000-09-20 13:22:33'}
        response = c.post('/api/chattinglog_send_message/', data=json.dumps(json4), content_type='json')
        self.assertEqual(response.status_code, 201)
        json5 = {'client_id': '5','service_id': '1','content': 'ferg','is_client': 1,'time': '2017-08-11 21:18:09'}
        response = c.post('/api/chattinglog_send_message/', data=json.dumps(json5), content_type='json')
        self.assertEqual(response.status_code, 200)


class Test_chattinglog_delete_record(TestCase):   
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

    def test(self):
        c = Client()
        response = c.post('/api/chattinglog_delete_record/')
        self.assertEqual(response.status_code, 201)
        service_instance = CustomerService.objects.get(id=1)
        ChattingLog.objects.create(id=1,client_id='1',service_id=service_instance,content='hahaha',is_client=1,time='2017-08-11 13:33:33')
        response = c.post('/api/chattinglog_delete_record/')
        self.assertEqual(response.status_code, 200)
        response = c.post('/api/chattinglog_delete_record/')
        self.assertEqual(response.status_code, 201)
        ChattingLog.objects.create(id=2,client_id='2',service_id=service_instance,content='hahaha',is_client=1,time='2017-08-11 13:33:33')
        ChattingLog.objects.create(id=3,client_id='3',service_id=service_instance,content='hahaha',is_client=0,time='2017-08-11 13:33:33')
        ChattingLog.objects.create(id=4,client_id='4',service_id=service_instance,content='hahaha',is_client=1,time='2017-08-11 13:33:33')
        response = c.post('/api/chattinglog_delete_record/')
        self.assertEqual(response.status_code, 200)
        response = c.post('/api/chattinglog_delete_record/')
        self.assertEqual(response.status_code, 201)


class Test_chattinglog_delete_record_ontime(TestCase):   
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

    def test(self):
        c = Client()
        response = c.post('/api/chattinglog_delete_record_ontime/')
        self.assertEqual(response.status_code, 201)
        service_instance = CustomerService.objects.get(id=1)
        ChattingLog.objects.create(id=1,client_id='1',service_id=service_instance,content='hahaha',is_client=1)
        response = c.post('/api/chattinglog_delete_record_ontime/')
        self.assertEqual(response.status_code, 201)
        ChattingLog.objects.create(id=2,client_id='2',service_id=service_instance,content='hahaha',is_client=1)
        ChattingLog.objects.create(id=3,client_id='3',service_id=service_instance,content='hahaha',is_client=0)
        ChattingLog.objects.create(id=4,client_id='4',service_id=service_instance,content='hahaha',is_client=1)
        response = c.post('/api/chattinglog_delete_record_ontime/')
        self.assertEqual(response.status_code, 201)
        ChattingLog.objects.create(id=5,client_id='2',service_id=service_instance,content='hahaha',is_client=1)
        ChattingLog.objects.create(id=6,client_id='3',service_id=service_instance,content='hahaha',is_client=0)
        ChattingLog.objects.create(id=7,client_id='4',service_id=service_instance,content='hahaha',is_client=1)
        response = c.post('/api/chattinglog_delete_record_ontime/')
        self.assertEqual(response.status_code, 201)
        response = c.post('/api/chattinglog_delete_record_ontime/')
        self.assertEqual(response.status_code, 201)


class Test_chattinglog_show_history(TestCase):   
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')
        

    def test(self):
        c = Client()        
        json1 = {'client_id': '1','service_id': '1'}
        response = c.post('/api/chattinglog_show_history/', data=json.dumps(json1), content_type='json')
        self.assertEqual(response.status_code, 201)
        service_instance = CustomerService.objects.get(id=1)
        ChattingLog.objects.create(id=1,client_id='1',service_id=service_instance,content='hahaha',is_client=1)
        json2 = {'client_id': '1','service_id': '1'}
        response = c.post('/api/chattinglog_show_history/', data=json.dumps(json2), content_type='json')
        self.assertEqual(response.status_code, 200)
        json3 = {'client_id': '3','service_id': '2'}
        response = c.post('/api/chattinglog_show_history/', data=json.dumps(json3), content_type='json')
        self.assertEqual(response.status_code, 201)
        ChattingLog.objects.create(id=2,client_id='8',service_id=service_instance,content='hahaha',is_client=1)
        json4 = {'client_id': '8','service_id': '1'}
        response = c.post('/api/chattinglog_show_history/', data=json.dumps(json4), content_type='json')
        self.assertEqual(response.status_code, 200)
