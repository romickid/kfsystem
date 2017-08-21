from django.test import TestCase
from django.test import Client
from ..views_helper_functions import *
from ..views_check_functions import *
from ..models import Admin, CustomerService, ChattingLog, SerialNumber, EnterpriseDisplayInfo
from ..serializers import AdminSerializer, CustomerServiceSerializer, CustomerServiceCreateSerializer, ChattingLogSerializer, SerialNumberSerializer, EnterpriseDisplayInfoSerializer
import json, time
from django.utils import timezone


class TestAdminCreate(TestCase):
    def setUp(self):
        SerialNumber.objects.create(serials='s1', is_used=False)
        SerialNumber.objects.create(serials="s2", is_used=False)
        SerialNumber.objects.create(serials="s3", is_used=False)
        SerialNumber.objects.create(serials="s4", is_used=True)
        SerialNumber.objects.create(serials="s5", is_used=False)
        SerialNumber.objects.create(serials="s6", is_used=False)
        SerialNumber.objects.create(serials="s7", is_used=False)
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1", vid_createtime=timezone.now())
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email="cs1@test.com", enterprise=admin_instance, nickname="c_nick1", password="c_pass1", is_register=False, is_online=False, connection_num=0, vid="c_vid1", vid_createtime=timezone.now())

    def test(self):
        c = Client()

        json1 = {'email': 'test1@a.com', 'nickname': 'nick1', 'password': 'pass1', 'serials': 's1'}
        request1 = c.post("/api/admin_create/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")
        instance_admin = Admin.objects.get(email='test1@a.com')
        instance_robot = CustomerService.objects.get(email=instance_admin.nickname+'@robot.com')
        self.assertEqual(instance_admin.nickname+'&Robot', instance_robot.nickname)

        json2 = {'email': 'test2@a.com', 'nickname': 'nick2', 'password': 'pass2'}
        request2 = c.post("/api/admin_create/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'test3@a.com', 'nickname': 'nick3', 'password': 'pass3', 'serials': 's3', 'other': 'other'}
        request3 = c.post("/api/admin_create/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'email': 'test4@a.com', 'nickname': 'nick4', 'password': 'pass4', 'serials': 's4'}
        request4 = c.post("/api/admin_create/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, serials is invalid.')

        json5 = {'email': 'admin1@test.com', 'nickname': 'nick5', 'password': 'pass5', 'serials': 's5'}
        request5 = c.post("/api/admin_create/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, email has been registered.')

        json6 = {'email': 'cs1@test.com', 'nickname': 'nick6', 'password': 'pass6', 'serials': 's6'}
        request6 = c.post("/api/admin_create/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), "ERROR, email has been registered.")

        json7 = {'email': 'test7@a.com', 'nickname': 'a_nick1', 'password': 'pass7', 'serials': 's7'}
        request7 = c.post("/api/admin_create/", data=json.dumps(json7), content_type='json')
        self.assertEqual(request7.status_code, 200)
        self.assertEqual(request7.content.decode('utf-8'), "ERROR, nickname has been used.")


class TestAdminLogin(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")

    def test(self):
        c = Client()

        json1 = {'email': 'admin1@test.com', 'password': '31b693c3308ed2a66d1d1a17fff1bb7ebfe0d986af4d8190fe3f8c380347a3ff1cc8fa280d1598ea38428a4991d3793fb6e4d96ed6aab10d6b3a9b25ff2f7475'}
        request1 = c.post("/api/admin_login/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

        json2 = {'email': 'admin1@test.com'}
        request2 = c.post("/api/admin_login/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'admin1@test.com', 'password': 'pass1', 'other': 'other'}
        request3 = c.post("/api/admin_login/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'email': 'admin2@test.com', 'password': '31b693c3308ed2a66d1d1a17fff1bb7ebfe0d986af4d8190fe3f8c380347a3ff1cc8fa280d1598ea38428a4991d3793fb6e4d96ed6aab10d6b3a9b25ff2f7475'}
        request4 = c.post("/api/admin_login/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, wrong email or password.')

        json5 = {'email': 'admin1@test.com', 'password': '31b693c3308ed2a66d1d1a17fff1bb7ebfe0d986af4d8190fe3f8c380347a3ff1cc8fa280d1598ea38428a4991d3793fb6e4d96ed6aab10d6b3a9b25ff2f7474'}
        request5 = c.post("/api/admin_login/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email or password.')


class TestAdminResetPassword(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        # actual password: a_pass1

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        json1 = {'password': '31b693c3308ed2a66d1d1a17fff1bb7ebfe0d986af4d8190fe3f8c380347a3ff1cc8fa280d1598ea38428a4991d3793fb6e4d96ed6aab10d6b3a9b25ff2f7475', 'newpassword': '52289478fa8154f22a6dad25ca77c565365234017658d55f62f6cc32327008290b828f4a7d2dddd0f1a821161ae80aff9608cd2233044fa4c0a18fa7a9dc8856'}
        request1 = c.post("/api/admin_reset_password/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

        json2 = {'password': '31b693c3308ed2a66d1d1a17fff1bb7ebfe0d986af4d8190fe3f8c380347a3ff1cc8fa280d1598ea38428a4991d3793fb6e4d96ed6aab10d6b3a9b25ff2f7475'}
        request2 = c.post("/api/admin_reset_password/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'password': '31b693c3308ed2a66d1d1a17fff1bb7ebfe0d986af4d8190fe3f8c380347a3ff1cc8fa280d1598ea38428a4991d3793fb6e4d96ed6aab10d6b3a9b25ff2f7475', 'newpassword': '52289478fa8154f22a6dad25ca77c565365234017658d55f62f6cc32327008290b828f4a7d2dddd0f1a821161ae80aff9608cd2233044fa4c0a18fa7a9dc8856', 'other': 'other'}
        request3 = c.post("/api/admin_reset_password/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'password': '31b693c3308ed2a66d1d1a17fff1bb7ebfe0d986af4d8190fe3f8c380347a3ff1cc8fa280d1598ea38428a4991d3793fb6e4d96ed6aab10d6b3a9b25ff2f7476', 'newpassword': '52289478fa8154f22a6dad25ca77c565365234017658d55f62f6cc32327008290b828f4a7d2dddd0f1a821161ae80aff9608cd2233044fa4c0a18fa7a9dc8856'}
        request4 = c.post("/api/admin_reset_password/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, wrong email or password.')

        session['a_email'] = 'admin2@test.com'
        session.save()
        json5 = {'password': '31b693c3308ed2a66d1d1a17fff1bb7ebfe0d986af4d8190fe3f8c380347a3ff1cc8fa280d1598ea38428a4991d3793fb6e4d96ed6aab10d6b3a9b25ff2f7475', 'newpassword': '52289478fa8154f22a6dad25ca77c565365234017658d55f62f6cc32327008290b828f4a7d2dddd0f1a821161ae80aff9608cd2233044fa4c0a18fa7a9dc8856'}
        request5 = c.post("/api/admin_reset_password/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email.')

        session.delete()
        json6 = {'password': '31b693c3308ed2a66d1d1a17fff1bb7ebfe0d986af4d8190fe3f8c380347a3ff1cc8fa280d1598ea38428a4991d3793fb6e4d96ed6aab10d6b3a9b25ff2f7475', 'newpassword': '52289478fa8154f22a6dad25ca77c565365234017658d55f62f6cc32327008290b828f4a7d2dddd0f1a821161ae80aff9608cd2233044fa4c0a18fa7a9dc8856'}
        request6 = c.post("/api/admin_reset_password/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), 'ERROR, session is broken.')


class TestAdminForgetPasswordEmailRequest(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        # actual password: a_pass1

    def test(self):
        c = Client()

        json1 = {'email': 'admin1@test.com'}
        request1 = c.post("/api/admin_forget_password_email_request/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

        json2 = {}
        request2 = c.post("/api/admin_forget_password_email_request/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'admin1@test.com', 'other': 'other'}
        request3 = c.post("/api/admin_forget_password_email_request/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'email': 'admin2@test.com'}
        request4 = c.post("/api/admin_forget_password_email_request/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, wrong email.')


class TestAdminForgetPasswordCheckVid(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        Admin.objects.create(id=2, email="admin2@test.com", nickname="a_nick2", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl2", widget_url="a_weidgeturl2", mobile_url="a_mobileurl2", communication_key="a_key2", vid="a_vid2")
        # actual password: a_pass1

    def test(self):
        c = Client()

        json1 = {'email': 'admin1@test.com', 'vid': 'a_vid1'}
        request1 = c.post("/api/admin_forget_password_check_vid/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(len(request1.content.decode('utf-8')), 32)

        json2 = {'email': 'admin1@test.com'}
        request2 = c.post("/api/admin_forget_password_check_vid/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'admin1@test.com', 'vid': 'a_vid1', 'other': 'other'}
        request3 = c.post("/api/admin_forget_password_check_vid/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'email': 'admin2@test.com', 'vid': 'a_vid1'}
        request4 = c.post("/api/admin_forget_password_check_vid/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, wrong email or vid.')

        json5 = {'email': 'admin1@test.com', 'vid': 'a_vid2'}
        request5 = c.post("/api/admin_forget_password_check_vid/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email or vid.')

        instance = Admin.objects.get(id=2)
        instance.vid_createtime = timezone.now() - timezone.timedelta(days=3)
        instance.save()
        json6 = {'email': 'admin2@test.com', 'vid': 'a_vid2'}
        request6 = c.post("/api/admin_forget_password_check_vid/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), 'ERROR, vid is expired.')


class TestAdminForgetPasswordSaveData(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        Admin.objects.create(id=2, email="admin2@test.com", nickname="a_nick2", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl2", widget_url="a_weidgeturl2", mobile_url="a_mobileurl2", communication_key="a_key2", vid="a_vid2")
        # actual password: a_pass1

    def test(self):
        c = Client()

        json1 = {'email': 'admin1@test.com', 'newpassword': '52289478fa8154f22a6dad25ca77c565365234017658d55f62f6cc32327008290b828f4a7d2dddd0f1a821161ae80aff9608cd2233044fa4c0a18fa7a9dc8856', 'vid': 'a_vid1'}
        request1 = c.post("/api/admin_forget_password_save_data/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), 'OK')
        instance = Admin.objects.get(id=1)
        self.assertEqual(instance.password, '2a7d6061cf267bea9d1264aaa11e6cdc52b0e09a57292b368f885ca274a7de5038921d8fbbac91343a2dbbf127fd8ca4d022ac95e2d4b1905df1a0bd5aaa10f3')

        json2 = {'email': 'admin1@test.com', 'newpassword': '52289478fa8154f22a6dad25ca77c565365234017658d55f62f6cc32327008290b828f4a7d2dddd0f1a821161ae80aff9608cd2233044fa4c0a18fa7a9dc8856'}
        request2 = c.post("/api/admin_forget_password_save_data/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'email': 'admin1@test.com', 'newpassword': '52289478fa8154f22a6dad25ca77c565365234017658d55f62f6cc32327008290b828f4a7d2dddd0f1a821161ae80aff9608cd2233044fa4c0a18fa7a9dc8856', 'vid': 'a_vid1', 'other': 'other'}
        request3 = c.post("/api/admin_forget_password_save_data/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'email': 'admin2@test.com', 'newpassword': '52289478fa8154f22a6dad25ca77c565365234017658d55f62f6cc32327008290b828f4a7d2dddd0f1a821161ae80aff9608cd2233044fa4c0a18fa7a9dc8856', 'vid': 'a_vid1'}
        request4 = c.post("/api/admin_forget_password_save_data/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, wrong email or vid.')

        json5 = {'email': 'admin1@test.com', 'newpassword': '52289478fa8154f22a6dad25ca77c565365234017658d55f62f6cc32327008290b828f4a7d2dddd0f1a821161ae80aff9608cd2233044fa4c0a18fa7a9dc8856', 'vid': 'a_vid2'}
        request5 = c.post("/api/admin_forget_password_save_data/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, wrong email or vid.')

        instance = Admin.objects.get(id=2)
        instance.vid_createtime = timezone.now() - timezone.timedelta(days=3)
        instance.save()
        json6 = {'email': 'admin2@test.com', 'newpassword': '52289478fa8154f22a6dad25ca77c565365234017658d55f62f6cc32327008290b828f4a7d2dddd0f1a821161ae80aff9608cd2233044fa4c0a18fa7a9dc8856', 'vid': 'a_vid2'}
        request6 = c.post("/api/admin_forget_password_save_data/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), 'ERROR, vid is expired.')


class TestAdminShowCommunicationKey(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        # actual password: a_pass1

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        request1 = c.post("/api/admin_show_communication_key/")
        self.assertEqual(request1.status_code, 200)
        instance = Admin.objects.get(id=1)
        # self.assertEqual(request1.content.decode('utf-8'), '{"communication_key": "' + instance.communication_key + '"}')

        session['a_email'] = 'admin2@test.com'
        session.save()
        request2 = c.post("/api/admin_show_communication_key/")
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, wrong email.")

        session.delete()
        request3 = c.post("/api/admin_show_communication_key/")
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, session is broken.')


class TestAdminResetCommunicationKey(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        # actual password: a_pass1

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        request1 = c.post("/api/admin_reset_communication_key/")
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")
        instance = Admin.objects.get(id=1)
        self.assertEqual(len(instance.communication_key), 32)

        session['a_email'] = 'admin2@test.com'
        session.save()
        request2 = c.post("/api/admin_reset_communication_key/")
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, wrong email.")

        session.delete()
        request3 = c.post("/api/admin_reset_communication_key/")
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, session is broken.')


class TestAdminShowCsStatus(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        # actual password: a_pass1
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email="cs1@test.com", enterprise=admin_instance, nickname="c_nick1", password="c_pass1", is_register=False, is_online=False, connection_num=0, vid="c_vid1")
        CustomerService.objects.create(id=2, email="cs2@test.com", enterprise=admin_instance, nickname="c_nick2", password="c_pass2", is_register=False, is_online=False, connection_num=0, vid="c_vid2")

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        request1 = c.post("/api/admin_show_cs_status/")
        self.assertEqual(request1.status_code, 200)

        session['a_email'] = 'admin2@test.com'
        session.save()
        request2 = c.post("/api/admin_show_cs_status/")
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, wrong email.")

        session.delete()
        request3 = c.post("/api/admin_show_cs_status/")
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, session is broken.')


class TestAdminDeleteCs(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        Admin.objects.create(id=2, email='admin2@test.com', nickname='a_nick2', password='a_pass2', web_url='a_weburl2', widget_url='a_widgeturl2', mobile_url='a_mobileurl2', communication_key='a_key2', vid='a_vid2')
        admin_instance1 = Admin.objects.get(id=1)
        admin_instance2 = Admin.objects.get(id=2)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance1, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance2, nickname='c_nick2', password='c_pass2', is_register=True, is_online=False, connection_num=0, vid='c_vid2')
        cs_instance1 = CustomerService.objects.get(id=1)
        cs_instance2 = CustomerService.objects.get(id=2)
        ChattingLog.objects.create(id=1, client_id='client1', service_id=cs_instance1, content='content1', is_client=False)
        ChattingLog.objects.create(id=2, client_id='client2', service_id=cs_instance2, content='content2', is_client=False)

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        json1 = {'email': 'cs1@test.com'}
        request1 = c.post("/api/admin_delete_cs/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), 'OK')
        cs_exist = CustomerService.objects.filter(email='cs1@test.com').exists()
        cl_exist = ChattingLog.objects.filter(service_id=1).exists()
        self.assertEqual(cs_exist, False)
        self.assertEqual(cl_exist, False)

        json2 = {}
        request2 = c.post("/api/admin_delete_cs/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@test.com', 'other': 'other'}
        request3 = c.post("/api/admin_delete_cs/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, wrong information.')

        json4 = {'email': 'cs3@test.com'}
        request4 = c.post("/api/admin_delete_cs/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), 'ERROR, wrong customerservice email.')

        json5 = {'email': 'cs2@test.com'}
        request5 = c.post("/api/admin_delete_cs/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, customerservice is not belong to admin.')

        session['a_email'] = 'admin3@a.com'
        session.save()
        json6 = {'email': 'cs1@test.com'}
        request6 = c.post("/api/admin_delete_cs/", data=json.dumps(json6), content_type='json')
        self.assertEqual(request6.status_code, 200)
        self.assertEqual(request6.content.decode('utf-8'), 'ERROR, wrong admin email.')

        session.delete()
        json7 = {'email': 'cs1@test.com'}
        request7 = c.post("/api/admin_delete_cs/", data=json.dumps(json7), content_type='json')
        self.assertEqual(request7.status_code, 200)
        self.assertEqual(request7.content.decode('utf-8'), 'ERROR, session is broken.')


class TestAdminShowUserStatus(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        # actual password: a_pass1

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        request1 = c.post("/api/admin_show_user_status/")
        self.assertEqual(request1.status_code, 200)
        instance = Admin.objects.get(id=1)
        # self.assertEqual(request1.content.decode('utf-8'), '{"email": "'+instance.email+'", "nickname": "'+instance.nickname+'"}')

        session['a_email'] = 'admin2@test.com'
        session.save()
        request2 = c.post("/api/admin_show_user_status/")
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, wrong email.")

        session.delete()
        request3 = c.post("/api/admin_show_user_status/")
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), 'ERROR, session is broken.')


class TestAdminDisplayInfoCreate(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        # actual password: a_pass1

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        json1 = {'name': 'info1', 'comment': 'this is info1'}
        request1 = c.post("/api/admin_display_info_create/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), 'OK')

        json2 = {'name': 'info2'}
        request2 = c.post("/api/admin_display_info_create/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'name': 'info3', 'comment': 'this is info3', 'other': 'other'}
        request3 = c.post("/api/admin_display_info_create/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), "ERROR, wrong information.")

        json11 = {'name': 'info1', 'comment': 'this is info11'}
        request11 = c.post("/api/admin_display_info_create/", data=json.dumps(json11), content_type='json')
        self.assertEqual(request11.status_code, 200)
        self.assertEqual(request11.content.decode('utf-8'), 'ERROR, attribute name has been used.')

        session['a_email'] = 'admin2@test.com'
        session.save()
        json4 = {'name': 'info4', 'comment': 'this is info4'}
        request4 = c.post("/api/admin_display_info_create/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), "ERROR, wrong email.")

        session.delete()
        json5 = {'name': 'info5', 'comment': 'this is info5'}
        request5 = c.post("/api/admin_display_info_create/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, session is broken.')


class TestAdminDisplayInfoDelete(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        instance = Admin.objects.get(id=1)
        EnterpriseDisplayInfo.objects.create(enterprise=instance, name='info1', comment='this is info1')
        EnterpriseDisplayInfo.objects.create(enterprise=instance, name='info2', comment='this is info2')
        # actual password: a_pass1

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        instance_admin = Admin.objects.get(id=1)
        instance_info = EnterpriseDisplayInfo.objects.get(enterprise=instance_admin.id, name='info1')
        instance_info_filter = EnterpriseDisplayInfo.objects.filter(enterprise=instance_admin.id)
        self.assertEqual(instance_info.name, 'info1')
        self.assertEqual(instance_info_filter.count(), 2)

        json1 = {'name': 'info1'}
        request1 = c.post("/api/admin_display_info_delete/", data=json.dumps(json1), content_type='json')
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), 'OK')
        
        instance_info_filter = EnterpriseDisplayInfo.objects.filter(enterprise=instance_admin.id)
        self.assertEqual(instance_info_filter.count(), 1)

        json2 = {}
        request2 = c.post("/api/admin_display_info_delete/", data=json.dumps(json2), content_type='json')
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(request2.content.decode('utf-8'), "ERROR, incomplete information.")

        json3 = {'name': 'info2', 'other': 'other'}
        request3 = c.post("/api/admin_display_info_delete/", data=json.dumps(json3), content_type='json')
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), "ERROR, wrong information.")

        session['a_email'] = 'admin2@test.com'
        session.save()
        json4 = {'name': 'info2'}
        request4 = c.post("/api/admin_display_info_delete/", data=json.dumps(json4), content_type='json')
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), "ERROR, wrong email.")

        session.delete()
        json5 = {'name': 'info2'}
        request5 = c.post("/api/admin_display_info_delete/", data=json.dumps(json5), content_type='json')
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, session is broken.')


class TestAdminDisplayInfoShow(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        Admin.objects.create(id=2, email="admin2@test.com", nickname="a_nick2", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl2", widget_url="a_weidgeturl2", mobile_url="a_mobileurl2", communication_key="a_key2", vid="a_vid2")
        instance = Admin.objects.get(id=1)
        EnterpriseDisplayInfo.objects.create(enterprise=instance, name='info1', comment='this is info1')
        EnterpriseDisplayInfo.objects.create(enterprise=instance, name='info2', comment='this is info2')
        # actual password: a_pass1

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        request1 = c.post("/api/admin_display_info_show/")
        self.assertEqual(request1.status_code, 200)

        session['a_email'] = 'admin2@test.com'
        session.save()
        request3 = c.post("/api/admin_display_info_show/")
        self.assertEqual(request3.status_code, 200)
        self.assertEqual(request3.content.decode('utf-8'), "ERROR, display info is empty.")

        session['a_email'] = 'admin3@test.com'
        session.save()
        request4 = c.post("/api/admin_display_info_show/")
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), "ERROR, wrong email.")

        session.delete()
        request5 = c.post("/api/admin_display_info_show/")
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, session is broken.')


class TestAdminLogout(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="03b7c09dc3533c22df04519db1d9b861e576356115da12682b39d8785885bc27ca566220c81a6abcd638e0da61d79474e2dfeeda3e86798d1374efbd6103e9b5", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        # actual password: a_pass1

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        request1 = c.post("/api/admin_logout/")
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request1.content.decode('utf-8'), "OK")

        c = Client()
        session = c.session
        session['a_email'] = 'admin2@test.com'
        session.save()
        request4 = c.post("/api/admin_logout/")
        self.assertEqual(request4.status_code, 200)
        self.assertEqual(request4.content.decode('utf-8'), "ERROR, wrong email.")

        session.delete()
        request5 = c.post("/api/admin_logout/")
        self.assertEqual(request5.status_code, 200)
        self.assertEqual(request5.content.decode('utf-8'), 'ERROR, session is broken.')
