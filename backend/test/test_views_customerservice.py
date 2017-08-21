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


class TestCsCreate(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email="cs1@test.com", enterprise=admin_instance, nickname="c_nick1", password="c_pass1", is_register=False, is_online=False, connection_num=0, vid="c_vid1")
        CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=True, is_online=False, connection_num=0, vid='c_vid2')
        
    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        json1 = {'email': 'test1@a.com'}
        request1 = c.post("/api/customerservice_create/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")
        instance = CustomerService.objects.get(email='test1@a.com')
        self.assertEqual(instance.is_register, False)

        json2 = {}
        request2 = c.post("/api/customerservice_create/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'test3@a.com', 'other': 'other'}
        request3 = c.post("/api/customerservice_create/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        session['a_email'] = 'admin2@test.com'
        session.save()
        json4 = {'email': 'test4@a.com'}
        request4 = c.post("/api/customerservice_create/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, admin_email is wrong.')

        session['a_email'] = 'admin1@test.com'
        session.save()
        json5 = {'email': 'admin1@test.com'}
        request5 = c.post("/api/customerservice_create/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, email has been registered.')

        json6 = {'email': 'cs2@test.com'}
        request6 = c.post("/api/customerservice_create/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, email has been registered.")

        json61 = {'email': 'cs1@test.com'}
        request61 = c.post("/api/customerservice_create/", data=json.dumps(json61), content_type='json')
        self.assertEqual(request61.status_code, 200)
        self.assertEqual(request61.content.decode('utf-8'), "OK")

        session.delete()
        json7 = {'email': 'cs1@test.com'}
        request7 = c.post("/api/customerservice_create/", data=json.dumps(json7), content_type='json')
        self.assertEqual(request7.status_code, 200)
        self.assertEqual(request7.content.decode('utf-8'), "ERROR, session is broken.")


class TestCsSetProfile(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=False, is_online=False, connection_num=0, vid='c_vid2')
        CustomerService.objects.create(id=3, email='cs3@test.com', enterprise=admin_instance, nickname='c_nick3', password='c_pass3', is_register=False, is_online=False, connection_num=0, vid='c_vid3')

    def test(self):
        c = Client()

        json1 = {'email': 'cs1@test.com', 'password': 'pass1', 'nickname': 'nick1', 'vid': 'c_vid1'}
        request1 = c.post("/api/customerservice_set_profile/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")
        instance = CustomerService.objects.get(email='cs1@test.com')
        self.assertEqual(instance.is_register, True)

        json2 = {'email': 'cs2@test.com', 'password': 'pass2', 'vid': 'c_vid2'}
        request2 = c.post("/api/customerservice_set_profile/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'cs2@test.com', 'password': 'pass2', 'nickname': 'nick2', 'vid': 'c_vid2', 'other': 'other'}
        request3 = c.post("/api/customerservice_set_profile/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'email': 'cs2@test.com', 'password': 'pass2', 'nickname': 'nick1', 'vid': 'c_vid2'}
        request4 = c.post("/api/customerservice_set_profile/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, nickname has been used.')

        json5 = {'email': 'cs3@a.com', 'password': 'pass2', 'nickname': 'nick2', 'vid': 'c_vid2'}
        request5 = c.post("/api/customerservice_set_profile/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email or vid.')

        json6 = {'email': 'cs2@test.com', 'password': 'pass2', 'nickname': 'nick2', 'vid': 'c_vid3'}
        request6 = c.post("/api/customerservice_set_profile/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, wrong email or vid.")

        instance = CustomerService.objects.get(id=3)
        instance.vid_createtime = timezone.now() - timezone.timedelta(days=3)
        instance.save()
        json7 = {'email': 'cs3@test.com', 'password': 'pass3', 'nickname': 'nick3', 'vid': 'c_vid3'}
        request7 = c.post("/api/customerservice_set_profile/", data=json.dumps(json7), content_type='json')
        self.assertEqual(request7.status_code, 200)
        self.assertEqual(request7.content.decode('utf-8'), "ERROR, vid is expired.")


class TestCsSetProfileCheckVid(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=False, is_online=False, connection_num=0, vid='c_vid2')
        CustomerService.objects.create(id=3, email='cs3@test.com', enterprise=admin_instance, nickname='c_nick3', password='c_pass3', is_register=False, is_online=False, connection_num=0, vid='c_vid3')

    def test(self):
        c = Client()

        json1 = {'email': 'cs1@test.com', 'vid': 'c_vid1'}
        request1 = c.post("/api/customerservice_set_profile_check_vid/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(len(request1.content.decode('utf-8')), 32)

        json2 = {'email': 'cs2@test.com'}
        request2 = c.post("/api/customerservice_set_profile_check_vid/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'cs2@test.com', 'vid': 'c_vid2', 'other': 'other'}
        request3 = c.post("/api/customerservice_set_profile_check_vid/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json5 = {'email': 'cs3@a.com', 'vid': 'c_vid2'}
        request5 = c.post("/api/customerservice_set_profile_check_vid/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email or vid.')

        json6 = {'email': 'cs2@test.com', 'vid': 'c_vid3'}
        request6 = c.post("/api/customerservice_set_profile_check_vid/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, wrong email or vid.")

        instance = CustomerService.objects.get(id=3)
        instance.vid_createtime = timezone.now() - timezone.timedelta(days=3)
        instance.save()
        json7 = {'email': 'cs3@test.com', 'vid': 'c_vid3'}
        request7 = c.post("/api/customerservice_set_profile_check_vid/", data=json.dumps(json7), content_type='json')
        self.assertEqual(request7.status_code, 200)
        self.assertEqual(request7.content.decode('utf-8'), "ERROR, vid is expired.")


class TestCsLogin(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='d43276edca0ed3df2b6df0bbe8b5b8c843ffd8921533192df786b66fd21517e1be030dcee21e1295ac325d5cfa56971f88c0538c7186e08461cdc18142097aea', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        c = Client()

        json1 = {'email': 'cs1@test.com', 'password': 'a117b51092404a9cd7bc9e57d56307d4dc629572307fe39c8d0eac0212249a927173809031198499f0464a3ea49db3e3df4f9a6e1ff3515bbaa51b316b030b93'}
        request1 = c.post("/api/customerservice_login/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")
        instance = CustomerService.objects.get(email='cs1@test.com')
        self.assertEqual(instance.is_online, True)

        json2 = {'email': 'cs1@test.com'}
        request2 = c.post("/api/customerservice_login/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'cs1@test.com', 'password': 'a117b51092404a9cd7bc9e57d56307d4dc629572307fe39c8d0eac0212249a927173809031198499f0464a3ea49db3e3df4f9a6e1ff3515bbaa51b316b030b93', 'other': 'other'}
        request3 = c.post("/api/customerservice_login/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json5 = {'email': 'cs1@test.com', 'password': 'b117b51092404a9cd7bc9e57d56307d4dc629572307fe39c8d0eac0212249a927173809031198499f0464a3ea49db3e3df4f9a6e1ff3515bbaa51b316b030b93'}
        request5 = c.post("/api/customerservice_login/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email or password.')

        json6 = {'email': 'cs2@test.com', 'password': 'a117b51092404a9cd7bc9e57d56307d4dc629572307fe39c8d0eac0212249a927173809031198499f0464a3ea49db3e3df4f9a6e1ff3515bbaa51b316b030b93'}
        request6 = c.post("/api/customerservice_login/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, wrong email or password.")


class TestCsResetPassword(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='d43276edca0ed3df2b6df0bbe8b5b8c843ffd8921533192df786b66fd21517e1be030dcee21e1295ac325d5cfa56971f88c0538c7186e08461cdc18142097aea', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance, nickname='c_nick2', password='e43276edca0ed3df2b6df0bbe8b5b8c843ffd8921533192df786b66fd21517e1be030dcee21e1295ac325d5cfa56971f88c0538c7186e08461cdc18142097aea', is_register=False, is_online=False, connection_num=0, vid='c_vid2')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        json1 = {'password': 'a117b51092404a9cd7bc9e57d56307d4dc629572307fe39c8d0eac0212249a927173809031198499f0464a3ea49db3e3df4f9a6e1ff3515bbaa51b316b030b93', 'newpassword': 'e35cea294062c3a0ee90cb2ae3405a824584cd9593bed76d40b3ba6099b4bc0c2696bf2b2c03ddbf67e3317a2293ddeb7670943ab977eb55a01c047831022dbb'}
        request1 = c.post("/api/customerservice_reset_password/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

        json2 = {'password': 'a117b51092404a9cd7bc9e57d56307d4dc629572307fe39c8d0eac0212249a927173809031198499f0464a3ea49db3e3df4f9a6e1ff3515bbaa51b316b030b93'}
        request2 = c.post("/api/customerservice_reset_password/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'password': 'a117b51092404a9cd7bc9e57d56307d4dc629572307fe39c8d0eac0212249a927173809031198499f0464a3ea49db3e3df4f9a6e1ff3515bbaa51b316b030b93', 'newpassword': 'e35cea294062c3a0ee90cb2ae3405a824584cd9593bed76d40b3ba6099b4bc0c2696bf2b2c03ddbf67e3317a2293ddeb7670943ab977eb55a01c047831022dbb', 'other': 'other'}
        request3 = c.post("/api/customerservice_reset_password/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'password': 'b117b51092404a9cd7bc9e57d56307d4dc629572307fe39c8d0eac0212249a927173809031198499f0464a3ea49db3e3df4f9a6e1ff3515bbaa51b316b030b93', 'newpassword': 'e35cea294062c3a0ee90cb2ae3405a824584cd9593bed76d40b3ba6099b4bc0c2696bf2b2c03ddbf67e3317a2293ddeb7670943ab977eb55a01c047831022dbb'}
        request4 = c.post("/api/customerservice_reset_password/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, wrong email or password.')

        session['c_email'] = 'cs2@test.com'
        session.save()
        json41 = {'password': 'a117b51092404a9cd7bc9e57d56307d4dc629572307fe39c8d0eac0212249a927173809031198499f0464a3ea49db3e3df4f9a6e1ff3515bbaa51b316b030b93', 'newpassword': 'e35cea294062c3a0ee90cb2ae3405a824584cd9593bed76d40b3ba6099b4bc0c2696bf2b2c03ddbf67e3317a2293ddeb7670943ab977eb55a01c047831022dbb'}
        request41 = c.post("/api/customerservice_reset_password/", data=json.dumps(json41), content_type='json')
        self.assertEqual(request41.status_code, 200)
        self.assertEqual(request41.content.decode('utf-8'), 'ERROR, wrong email or password.')

        session['c_email'] = 'cs3@test.com'
        session.save()
        json5 = {'password': 'a117b51092404a9cd7bc9e57d56307d4dc629572307fe39c8d0eac0212249a927173809031198499f0464a3ea49db3e3df4f9a6e1ff3515bbaa51b316b030b93', 'newpassword': 'e35cea294062c3a0ee90cb2ae3405a824584cd9593bed76d40b3ba6099b4bc0c2696bf2b2c03ddbf67e3317a2293ddeb7670943ab977eb55a01c047831022dbb'}
        request5 = c.post("/api/customerservice_reset_password/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email.')

        session.delete()
        json6 = {'password': 'a117b51092404a9cd7bc9e57d56307d4dc629572307fe39c8d0eac0212249a927173809031198499f0464a3ea49db3e3df4f9a6e1ff3515bbaa51b316b030b93', 'newpassword': 'e35cea294062c3a0ee90cb2ae3405a824584cd9593bed76d40b3ba6099b4bc0c2696bf2b2c03ddbf67e3317a2293ddeb7670943ab977eb55a01c047831022dbb'}
        request6 = c.post("/api/customerservice_reset_password/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, session is broken.")


class TestCsForgetPasswordEmailRequest(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        c = Client()

        json1 = {'email': 'cs1@test.com'}
        request1 = c.post("/api/customerservice_forget_password_email_request/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

        json2 = {}
        request2 = c.post("/api/customerservice_forget_password_email_request/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'cs1@test.com', 'other': 'other'}
        request3 = c.post("/api/customerservice_forget_password_email_request/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'email': 'cs2@test.com'}
        request4 = c.post("/api/customerservice_forget_password_email_request/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, wrong email.')


class TestCsForgetPasswordCheckVid(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=False, is_online=False, connection_num=0, vid='c_vid2')

    def test(self):
        c = Client()

        json1 = {'email': 'cs1@test.com', 'vid': 'c_vid1'}
        request1 = c.post("/api/customerservice_forget_password_check_vid/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(len(request1.content.decode('utf-8')), 32)
        instance = CustomerService.objects.get(id=1)
        self.assertEqual(instance.vid, request1.content.decode('utf-8'))

        json2 = {'email': 'cs1@test.com'}
        request2 = c.post("/api/customerservice_forget_password_check_vid/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'cs1@test.com', 'vid': 'c_vid1', 'other': 'other'}
        request3 = c.post("/api/customerservice_forget_password_check_vid/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'email': 'cs2@test.com', 'vid': 'c_vid1'}
        request4 = c.post("/api/customerservice_forget_password_check_vid/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, wrong email or vid.')

        json5 = {'email': 'cs1@test.com', 'vid': 'c_vid2'}
        request5 = c.post("/api/customerservice_forget_password_check_vid/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email or vid.')

        instance = CustomerService.objects.get(id=2)
        instance.vid_createtime = timezone.now() - timezone.timedelta(days=3)
        instance.save()
        json7 = {'email': 'cs2@test.com', 'vid': 'c_vid2'}
        request7 = c.post("/api/customerservice_forget_password_check_vid/", data=json.dumps(json7), content_type='json')
        self.assertEqual(request7.status_code, 200)
        self.assertEqual(request7.content.decode('utf-8'), 'ERROR, vid is expired.')


class TestCsForgetPasswordSaveData(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=False, is_online=False, connection_num=0, vid='c_vid2')

    def test(self):
        c = Client()

        json1 = {'email': 'cs1@test.com', 'newpassword': 'c_newpass1', 'vid': 'c_vid1'}
        request1 = c.post("/api/customerservice_forget_password_save_data/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), 'OK')

        json2 = {'email': 'cs1@test.com', 'vid': 'c_vid1'}
        request2 = c.post("/api/customerservice_forget_password_save_data/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'cs1@test.com', 'newpassword': 'c_newpass1', 'vid': 'c_vid1', 'other': 'other'}
        request3 = c.post("/api/customerservice_forget_password_save_data/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'email': 'cs2@test.com', 'newpassword': 'c_newpass1', 'vid': 'c_vid1'}
        request4 = c.post("/api/customerservice_forget_password_save_data/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, wrong email or vid.')

        json5 = {'email': 'cs1@test.com', 'newpassword': 'c_newpass1', 'vid': 'c_vid2'}
        request5 = c.post("/api/customerservice_forget_password_save_data/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email or vid.')

        instance = CustomerService.objects.get(id=2)
        instance.vid_createtime = timezone.now() - timezone.timedelta(days=3)
        instance.save()
        json7 = {'email': 'cs2@test.com', 'newpassword': 'c_newpass2', 'vid': 'c_vid2'}
        request7 = c.post("/api/customerservice_forget_password_save_data/", data=json.dumps(json7), content_type='json')
        self.assertEqual(request7.status_code, 200)
        self.assertEqual(request7.content.decode('utf-8'), 'ERROR, vid is expired.')


class TestCsShowUserStatus(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        request1 = c.post("/api/customerservice_show_user_status/")
        self.assertEqual(request1.status_code, 200)

        session['c_email'] = 'cs2@test.com'
        session.save()
        request2 = c.post("/api/customerservice_show_user_status/")
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, wrong email.")

        session.delete()
        request3 = c.post("/api/customerservice_show_user_status/")
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, session is broken.')


class TestCsUpdateConnectionNum(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        json1 = {'connection_num': 10}
        request1 = c.post("/api/customerservice_update_connection_num/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

        json2 = {}
        request2 = c.post("/api/customerservice_update_connection_num/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'connection_num': 10, 'other': 'other'}
        request3 = c.post("/api/customerservice_update_connection_num/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'connection_num': '10'}
        request4 = c.post("/api/customerservice_update_connection_num/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), "ERROR, wrong type.")

        session['c_email'] = 'cs2@test.com'
        session.save()
        json5 = {'connection_num': 10}
        request5 = c.post("/api/customerservice_update_connection_num/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email.')

        session.delete()
        json6 = {'connection_num': 10}
        request6 = c.post("/api/customerservice_update_connection_num/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, session is broken.")


class TestCsSetRobotInfoCreate(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        RobotInfo.objects.create(id=2, enterprise=admin_instance, question='question2', answer='answer1', keyword='keyword1', weight=0)

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        json1 = {'question': 'question1', 'answer': 'answer1', 'keyword': 'keyword1 keyword2', 'weight': 0}
        request1 = c.post("/api/customerservice_setrobotinfo_create/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

        json2 = {'question': 'question1', 'answer': 'answer1', 'weight': 0}
        request2 = c.post("/api/customerservice_setrobotinfo_create/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'question': 'question1', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0, 'other': 'other'}
        request3 = c.post("/api/customerservice_setrobotinfo_create/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'question': 'question2', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0}
        request4 = c.post("/api/customerservice_setrobotinfo_create/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), "ERROR, info is exist.")

        session['c_email'] = 'cs2@test.com'
        session.save()
        json5 = {'question': 'question3', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0}
        request5 = c.post("/api/customerservice_setrobotinfo_create/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email.')

        session.delete()
        json6 = {'question': 'question3', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0}
        request6 = c.post("/api/customerservice_setrobotinfo_create/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, session is broken.")


class TestCsSetRobotInfoDelete(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        RobotInfo.objects.create(id=1, enterprise=admin_instance, question='question1', answer='answer1', keyword='keyword1', weight=0)

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        json1 = {'question': 'question1'}
        request1 = c.post("/api/customerservice_setrobotinfo_delete/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

        json2 = {}
        request2 = c.post("/api/customerservice_setrobotinfo_delete/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'question': 'question1', 'other': 'other'}
        request3 = c.post("/api/customerservice_setrobotinfo_delete/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'question': 'question2'}
        request4 = c.post("/api/customerservice_setrobotinfo_delete/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), "ERROR, info is not exist.")

        session['c_email'] = 'cs2@test.com'
        session.save()
        json5 = {'question': 'question1'}
        request5 = c.post("/api/customerservice_setrobotinfo_delete/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email.')

        session.delete()
        json6 = {'question': 'question1'}
        request6 = c.post("/api/customerservice_setrobotinfo_delete/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, session is broken.")


class TestCsSetRobotInfoShow(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        RobotInfo.objects.create(id=1, enterprise=admin_instance, question='question1', answer='answer1', keyword='keyword1', weight=0)

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        request1 = c.post("/api/customerservice_setrobotinfo_show/")
        self.assertEqual(request1.status_code, 200)

        session['c_email'] = 'cs2@test.com'
        session.save()
        request5 = c.post("/api/customerservice_setrobotinfo_show/")
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email.')

        session.delete()
        request6 = c.post("/api/customerservice_setrobotinfo_show/")
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, session is broken.")


class TestCsDisplayrobotreplyShow(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        Admin.objects.create(id=2, email='admin2@test.com', nickname='a_nick2', password='a_pass2', web_url='a_weburl2', widget_url='a_widgeturl2', mobile_url='a_mobileurl2', communication_key='a_key2', vid='a_vid2')
        admin_instance1 = Admin.objects.get(id=1)
        admin_instance2 = Admin.objects.get(id=2)
        RobotInfo.objects.create(id=1, enterprise=admin_instance1, question='你好', answer='answer1', keyword='keyword1', weight=1)
        RobotInfo.objects.create(id=2, enterprise=admin_instance1, question='早安 上海', answer='answer2', keyword='keyword2', weight=1)
        RobotInfo.objects.create(id=3, enterprise=admin_instance1, question='早安 北京', answer='answer3', keyword='keyword3', weight=1)

    def test(self):
        c = Client()

        json1 = {'nickname': 'a_nick1', 'customer_input': '你好'}
        request1 = c.post("/api/customerservice_displayrobotreply_show/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        # self.assertEqual(request1.content.decode('utf-8'), "你好   answer1")

        json2 = {'nickname': 'a_nick1'}
        request2 = c.post("/api/customerservice_displayrobotreply_show/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'nickname': 'a_nick1', 'customer_input': 'morning', 'other': 'other'}
        request3 = c.post("/api/customerservice_displayrobotreply_show/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), "ERROR, wrong information.")

        json4 = {'nickname': 'a_nick2', 'customer_input': 'morning'}
        request4 = c.post("/api/customerservice_displayrobotreply_show/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        # self.assertEqual(request4.content.decode('utf-8'), "很抱歉，我不是很清楚您说的是什么，请尝试询问其他问题或使用人工客服。")


class TestCsLogout(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=True, is_online=True, connection_num=0, vid='c_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        request1 = c.post("/api/customerservice_logout/")
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")
        instance = CustomerService.objects.get(email='cs1@test.com')
        self.assertEqual(instance.is_online, False)

        session['c_email'] = 'cs2@test.com'
        session.save()
        request2 = c.post("/api/customerservice_logout/")
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, wrong email.")

        session.delete()
        request3 = c.post("/api/customerservice_logout/")
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, session is broken.')
