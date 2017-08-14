from django.test import TestCase
from django.test import Client
from .views_helper_functions import *
from .views_check_functions import *
from .models import Admin, CustomerService, ChattingLog, SerialNumber, ImageLog, EnterpriseDisplayInfo
from .serializers import AdminSerializer, CustomerServiceSerializer, CustomerServiceCreateSerializer, ChattingLogSerializer, SerialNumberSerializer, EnterpriseDisplayInfoSerializer
import json


class TestCsCreate(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email="cs1@test.com", enterprise=admin_instance, nickname="c_nick1", password="c_pass1", is_register=False, is_online=False, connection_num=0, vid="c_vid1")

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        json1 = {'email': 'test1@a.com'}
        request1 = c.post("/api/customerservice_create/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

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

        json6 = {'email': 'cs1@test.com'}
        request6 = c.post("/api/customerservice_create/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, email has been registered.")

        session.delete()
        json7 = {'email': 'cs1@test.com'}
        request7 = c.post("/api/customerservice_create/", data=json.dumps(json7), content_type='json')
        self.assertEqual(request7.status_code, 200)
        self.assertEqual(request7.content.decode('utf-8'), "ERROR, session is broken.")


class TestCsSetProfile(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@a.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=False, is_online=False, connection_num=0, vid='c_vid2')

    def test(self):
        c = Client()

        json1 = {'email': 'cs1@a.com', 'password': 'pass1', 'nickname': 'nick1', 'vid': 'c_vid1'}
        request1 = c.post("/api/customerservice_set_profile/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

        json2 = {'email': 'cs2@a.com', 'password': 'pass2', 'vid': 'c_vid2'}
        request2 = c.post("/api/customerservice_set_profile/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'cs2@a.com', 'password': 'pass2', 'nickname': 'nick2', 'vid': 'c_vid2', 'other': 'other'}
        request3 = c.post("/api/customerservice_set_profile/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'email': 'cs2@a.com', 'password': 'pass2', 'nickname': 'nick1', 'vid': 'c_vid2'}
        request4 = c.post("/api/customerservice_set_profile/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, nickname has been used.')

        json5 = {'email': 'cs3@a.com', 'password': 'pass2', 'nickname': 'nick2', 'vid': 'c_vid2'}
        request5 = c.post("/api/customerservice_set_profile/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email or vid.')

        json6 = {'email': 'cs2@a.com', 'password': 'pass2', 'nickname': 'nick2', 'vid': 'c_vid3'}
        request6 = c.post("/api/customerservice_set_profile/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, wrong email or vid.")


class TestCsSetProfileCheckVid(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@a.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=False, is_online=False, connection_num=0, vid='c_vid2')

    def test(self):
        c = Client()

        json1 = {'email': 'cs1@a.com', 'vid': 'c_vid1'}
        request1 = c.post("/api/customerservice_set_profile_check_vid/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(len(request1.content.decode('utf-8')), 32)

        json2 = {'email': 'cs2@a.com'}
        request2 = c.post("/api/customerservice_set_profile_check_vid/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'cs2@a.com', 'vid': 'c_vid2', 'other': 'other'}
        request3 = c.post("/api/customerservice_set_profile_check_vid/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json5 = {'email': 'cs3@a.com', 'vid': 'c_vid2'}
        request5 = c.post("/api/customerservice_set_profile_check_vid/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email or vid.')

        json6 = {'email': 'cs2@a.com', 'vid': 'c_vid3'}
        request6 = c.post("/api/customerservice_set_profile_check_vid/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, wrong email or vid.")


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

    def test(self):
        c = Client()

        json1 = {'email': 'cs1@test.com', 'vid': 'c_vid1'}
        request1 = c.post("/api/customerservice_forget_password_check_vid/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(len(request1.content.decode('utf-8')), 32)

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


class TestCsForgetPasswordSaveData(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

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


class TestCsRobotInfoCreate(TestCase):
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

        json1 = {'question': 'question1', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0}
        request1 = c.post("/api/customerservice_robotinfo_create/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

        json2 = {'question': 'question1', 'answer': 'answer1', 'weight': 0}
        request2 = c.post("/api/customerservice_robotinfo_create/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'question': 'question1', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0, 'other': 'other'}
        request3 = c.post("/api/customerservice_robotinfo_create/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'question': 'question2', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0}
        request4 = c.post("/api/customerservice_robotinfo_create/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), "ERROR, info is exist.")

        session['c_email'] = 'cs2@a.com'
        session.save()
        json5 = {'question': 'question3', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0}
        request5 = c.post("/api/customerservice_robotinfo_create/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email.')

        session.delete()
        json6 = {'question': 'question3', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0}
        request6 = c.post("/api/customerservice_robotinfo_create/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, session is broken.")


class TestCsRobotInfoDelete(TestCase):
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
        request1 = c.post("/api/customerservice_robotinfo_delete/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

        json2 = {}
        request2 = c.post("/api/customerservice_robotinfo_delete/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'question': 'question1', 'other': 'other'}
        request3 = c.post("/api/customerservice_robotinfo_delete/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'question': 'question2'}
        request4 = c.post("/api/customerservice_robotinfo_delete/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), "ERROR, info is not exist.")

        session['c_email'] = 'cs2@a.com'
        session.save()
        json5 = {'question': 'question1'}
        request5 = c.post("/api/customerservice_robotinfo_delete/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email.')

        session.delete()
        json6 = {'question': 'question1'}
        request6 = c.post("/api/customerservice_robotinfo_delete/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, session is broken.")


class TestCsRobotInfoShow(TestCase):
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

        request1 = c.post("/api/customerservice_robotinfo_show/")
        self.assertEqual(request1.status_code, 200)

        session['c_email'] = 'cs2@a.com'
        session.save()
        request5 = c.post("/api/customerservice_robotinfo_show/")
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email.')

        session.delete()
        request6 = c.post("/api/customerservice_robotinfo_show/")
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, session is broken.")


class TestCsLogout(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        request1 = c.post("/api/customerservice_logout/")
        self.assertEqual(request1.status_code, 200)

        session['c_email'] = 'cs2@test.com'
        session.save()
        request2 = c.post("/api/customerservice_logout/")
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, wrong email.")

        session.delete()
        request3 = c.post("/api/customerservice_logout/")
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, session is broken.')
