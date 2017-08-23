from django.test import TestCase
from django.test.client import Client
from ..views_helper_functions import *
from ..views_check_functions import *
from ..models import Admin, CustomerService, ChattingLog, SerialNumber, EnterpriseDisplayInfo, RobotInfo
from django.utils import timezone
import datetime


class TestAdminCreateCheck(TestCase):
    def setUp(self):
        SerialNumber.objects.create(serials='s1', is_used=False)
        SerialNumber.objects.create(serials='s2', is_used=False)
        SerialNumber.objects.create(serials='s3', is_used=False)
        SerialNumber.objects.create(serials='s4', is_used=True)
        SerialNumber.objects.create(serials='s5', is_used=False)
        SerialNumber.objects.create(serials='s6', is_used=False)
        SerialNumber.objects.create(serials='s7', is_used=False)
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        json1 = {'email': 'test1@a.com', 'nickname': 'nick1', 'password': 'pass1', 'serials': 's1'}
        errorcode1, errormessage1 = admin_create_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'test2@a.com', 'nickname': 'nick2', 'password': 'pass2'}
        errorcode2, errormessage2 = admin_create_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'test3@a.com', 'nickname': 'nick3', 'password': 'pass3', 'serials': 's3', 'other': 'other'}
        errorcode3, errormessage3 = admin_create_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'test4@a.com', 'nickname': 'nick4', 'password': 'pass4', 'serials': 's4'}
        errorcode4, errormessage4 = admin_create_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, serials is invalid.')

        json5 = {'email': 'admin1@test.com', 'nickname': 'nick5', 'password': 'pass5', 'serials': 's5'}
        errorcode5, errormessage5 = admin_create_check(json5)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, email has been registered.')

        json6 = {'email': 'cs1@test.com', 'nickname': 'nick6', 'password': 'pass6', 'serials': 's6'}
        errorcode6, errormessage6 = admin_create_check(json6)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, email has been registered.')

        json7 = {'email': 'test7@a.com', 'nickname': 'a_nick1', 'password': 'pass7', 'serials': 's7'}
        errorcode7, errormessage7 = admin_create_check(json7)
        self.assertEqual(errorcode7, 0)
        self.assertEqual(errormessage7, 'ERROR, nickname has been used.')


class TestAdminLoginCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        json1 = {'email': 'admin1@test.com', 'password': 'a_pass1'}
        errorcode1, errormessage1 = admin_login_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'admin1@test.com'}
        errorcode2, errormessage2 = admin_login_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'admin1@test.com', 'nickname': 'nick3', 'password': 'a_pass1'}
        errorcode3, errormessage3 = admin_login_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')


class TestAdminResetPasswordCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        json1 = {'password': 'a_pass1', 'newpassword': 'Anewpass1'}
        errorcode1, errormessage1 = admin_reset_password_check(json1, c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'password': 'a_pass1'}
        errorcode2, errormessage2 = admin_reset_password_check(json2, c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'password': 'a_pass1', 'newpassword': 'Anewpass1', 'other': 'other'}
        errorcode3, errormessage3 = admin_reset_password_check(json3, c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'password': 'a_pass1', 'newpassword': 'Anewpass1'}
        session['a_email'] = 'admin2@a.com'
        session.save()
        errorcode4, errormessage4 = admin_reset_password_check(json4, c)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email.')

        json5 = {'password': 'a_pass1', 'newpassword': 'Anewpass1'}
        session.delete()
        errorcode5, errormessage5 = admin_reset_password_check(json5, c)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, session is broken.')


class TestAdminForgetPasswordEmailRequestCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        json1 = {'email': 'admin1@test.com'}
        errorcode1, errormessage1 = admin_forget_password_email_request_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {}
        errorcode2, errormessage2 = admin_forget_password_email_request_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'admin1@test.com', 'password': 'a_pass1'}
        errorcode3, errormessage3 = admin_forget_password_email_request_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'admin2@a.com'}
        errorcode4, errormessage4 = admin_forget_password_email_request_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email.')


class TestAdminForgetPasswordCheckVidCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        json1 = {'email': 'admin1@test.com', 'vid': 'a_vid1'}
        errorcode1, errormessage1 = admin_forget_password_check_vid_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'admin1@test.com'}
        errorcode2, errormessage2 = admin_forget_password_check_vid_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'admin1@test.com', 'password': 'a_pass1', 'vid': 'a_vid1'}
        errorcode3, errormessage3 = admin_forget_password_check_vid_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'admin2@a.com', 'vid': 'a_vid1'}
        errorcode4, errormessage4 = admin_forget_password_check_vid_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email or vid.')

        json5 = {'email': 'admin1@test.com', 'vid': 'vid1'}
        errorcode5, errormessage5 = admin_forget_password_check_vid_check(json5)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email or vid.')

        instance = Admin.objects.get(id=1)
        instance.vid_createtime = timezone.now() - timezone.timedelta(days=3)
        instance.save()
        json6 = {'email': 'admin1@test.com', 'vid': 'a_vid1'}
        errorcode6, errormessage6 = admin_forget_password_check_vid_check(json6)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, vid is expired.')


class TestAdminForgetPasswordSaveDataCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        json1 = {'email': 'admin1@test.com', 'newpassword': 'Anewpass1', 'vid': 'a_vid1'}
        errorcode1, errormessage1 = admin_forget_password_save_data_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'admin1@test.com', 'newpassword': 'Anewpass1'}
        errorcode2, errormessage2 = admin_forget_password_save_data_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'admin1@test.com', 'newpassword': 'Anewpass1', 'vid': 'a_vid1', 'other': 'other'}
        errorcode3, errormessage3 = admin_forget_password_save_data_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'admin2@a.com', 'newpassword': 'Anewpass1', 'vid': 'a_vid1'}
        errorcode4, errormessage4 = admin_forget_password_save_data_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email or vid.')

        json5 = {'email': 'admin1@test.com', 'newpassword': 'Anewpass1', 'vid': 'Avid2'}
        errorcode5, errormessage5 = admin_forget_password_save_data_check(json5)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email or vid.')

        instance = Admin.objects.get(id=1)
        instance.vid_createtime = timezone.now() - timezone.timedelta(days=3)
        instance.save()
        json6 = {'email': 'admin1@test.com', 'newpassword': 'Anewpass1', 'vid': 'a_vid1'}
        errorcode6, errormessage6 = admin_forget_password_save_data_check(json6)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, vid is expired.')


class TestAdminShowCommunicationKeyCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        errorcode1, errormessage1 = admin_show_communication_key_check(c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        session['a_email'] = 'admin2@a.com'
        session.save()
        errorcode2, errormessage2 = admin_show_communication_key_check(c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        session.delete()
        errorcode3, errormessage3 = admin_show_communication_key_check(c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')




class TestAdminResetCommunicationKeyCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        errorcode1, errormessage1 = admin_reset_communication_key_check(c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        session['a_email'] = 'admin2@a.com'
        session.save()
        errorcode2, errormessage2 = admin_reset_communication_key_check(c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        session.delete()
        errorcode3, errormessage3 = admin_reset_communication_key_check(c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')


class TestAdminShowCsStatusCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        errorcode1, errormessage1 = admin_show_cs_status_check(c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        session['a_email'] = 'admin2@a.com'
        session.save()
        errorcode2, errormessage2 = admin_show_cs_status_check(c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        session.delete()
        errorcode3, errormessage3 = admin_show_cs_status_check(c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')


class TestAdminDeleteCsCheck(TestCase):
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
        errorcode1, errormessage1 = admin_delete_cs_check(json1, c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {}
        errorcode2, errormessage2 = admin_delete_cs_check(json2, c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@test.com', 'other': 'other'}
        errorcode3, errormessage3 = admin_delete_cs_check(json3, c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'cs3@test.com'}
        errorcode4, errormessage4 = admin_delete_cs_check(json4, c)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong customerservice email.')

        json5 = {'email': 'cs2@test.com'}
        errorcode5, errormessage5 = admin_delete_cs_check(json5, c)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, customerservice is not belong to admin.')

        session['a_email'] = 'admin3@a.com'
        session.save()
        json6 = {'email': 'cs1@test.com'}
        errorcode6, errormessage6 = admin_delete_cs_check(json6, c)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, wrong admin email.')

        session.delete()
        json7 = {'email': 'cs1@test.com'}
        errorcode7, errormessage7 = admin_delete_cs_check(json7, c)
        self.assertEqual(errorcode7, 0)
        self.assertEqual(errormessage7, 'ERROR, session is broken.')


class TestAdminShowUserStatusCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        errorcode1, errormessage1 = admin_show_user_status_check(c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        session['a_email'] = 'admin2@a.com'
        session.save()
        errorcode2, errormessage2 = admin_show_user_status_check(c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        session.delete()
        errorcode3, errormessage3 = admin_show_user_status_check(c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')


class TestAdminShowUrlStatusCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        errorcode1, errormessage1 = admin_show_url_status_check(c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        session['a_email'] = 'admin2@a.com'
        session.save()
        errorcode2, errormessage2 = admin_show_url_status_check(c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        session.delete()
        errorcode3, errormessage3 = admin_show_url_status_check(c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')


class TestAdminDisplayInfoCreateCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        instance = Admin.objects.get(id=1)
        EnterpriseDisplayInfo.objects.create(id=1, enterprise=instance, name='id_used', comment='this is id')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        json1 = {'name': 'id', 'comment': 'this is id'}
        errorcode1, errormessage1 = admin_display_info_create_check(json1, c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'name': 'id', 'comment': 'this is id'}
        session['a_email'] = 'admin2@a.com'
        session.save()
        errorcode2, errormessage2 = admin_display_info_create_check(json2, c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        json3 = {'name': 'id', 'comment': 'this is id'}
        session.delete()
        errorcode3, errormessage3 = admin_display_info_create_check(json3, c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')

        c1 = Client()
        session1 = c1.session
        session1['a_email'] = 'admin1@test.com'
        session1.save()
        json4 = {'name': 'id_used', 'comment': 'this is id'}
        errorcode4, errormessage4 = admin_display_info_create_check(json4, c1)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, attribute name has been used.')


class TestAdminDisplayInfoDeleteCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        instance = Admin.objects.get(id=1)
        EnterpriseDisplayInfo.objects.create(id=1, enterprise=instance, name='id_used', comment='this is id')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        json1 = {'name': 'id_used'}
        errorcode1, errormessage1 = admin_display_info_delete_check(json1, c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'name': 'id_used'}
        session['a_email'] = 'admin2@a.com'
        session.save()
        errorcode2, errormessage2 = admin_display_info_delete_check(json2, c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        json3 = {'name': 'id_used'}
        session.delete()
        errorcode3, errormessage3 = admin_display_info_delete_check(json3, c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')

        c1 = Client()
        session1 = c1.session
        session1['a_email'] = 'admin1@test.com'
        session1.save()
        json4 = {'name': 'id'}
        errorcode4, errormessage4 = admin_display_info_delete_check(json4, c1)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, attribute is not existent.')


class TestAdminDisplayInfoShowCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        Admin.objects.create(id=2, email='admin2@a.com', nickname='Anick2', password='Apass2', web_url='Aweb_url2', widget_url='Awidget_url2', mobile_url='Amobile_url2', communication_key='Akey2', vid='Avid2')
        instance = Admin.objects.get(id=1)
        EnterpriseDisplayInfo.objects.create(id=1, enterprise=instance, name='id_used', comment='this is id')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        errorcode1, errormessage1 = admin_display_info_show_check(c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        session['a_email'] = 'admin_not_exist@a.com'
        session.save()
        errorcode2, errormessage2 = admin_display_info_show_check(c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        session.delete()
        errorcode3, errormessage3 = admin_display_info_show_check(c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')

        c1 = Client()
        session1 = c1.session
        session1['a_email'] = 'admin2@a.com'
        session1.save()
        errorcode4, errormessage4 = admin_display_info_show_check(c1)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, display info is empty.')


class TestAdminLogoutChekc(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        errorcode1, errormessage1 = admin_logout_check(c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        session['a_email'] = 'admin2@a.com'
        session.save()
        errorcode2, errormessage2 = admin_logout_check(c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        session.delete()
        errorcode3, errormessage3 = admin_logout_check(c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')


class TestCsCreateCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=True, is_online=False, connection_num=0, vid='c_vid2')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        json1 = {'email': 'test1@a.com'}
        errorcode1, errormessage1 = customerservice_create_check(json1, c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {}
        errorcode2, errormessage2 = customerservice_create_check(json2, c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'test1@a.com', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_create_check(json3, c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        session['a_email'] = 'admin2@a.com'
        session.save()
        json4 = {'email': 'test1@a.com'}
        errorcode4, errormessage4 = customerservice_create_check(json4, c)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, admin_email is wrong.')

        session.delete()
        json5 = {'email': 'test1@a.com'}
        errorcode5, errormessage5 = customerservice_create_check(json5, c)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, session is broken.')

        c1 = Client()
        session = c1.session
        session['a_email'] = 'admin1@test.com'
        session.save()

        json6 = {'email': 'cs2@test.com'}
        errorcode6, errormessage6 = customerservice_create_check(json6, c1)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, email has been registered.')

        json7 = {'email': 'admin1@test.com'}
        errorcode7, errormessage7 = customerservice_create_check(json7, c1)
        self.assertEqual(errorcode7, 0)
        self.assertEqual(errormessage7, 'ERROR, email has been registered.')


class TestCsSetProfileCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=False, is_online=False, connection_num=0, vid='c_vid2')

    def test(self):
        json1 = {'email': 'cs1@test.com', 'password': 't1_pass', 'nickname': 't1_nick', 'vid': 'c_vid1'}
        errorcode1, errormessage1 = customerservice_set_profile_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'cs1@test.com', 'password': 't1_pass', 'vid': 'c_vid1'}
        errorcode2, errormessage2 = customerservice_set_profile_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@test.com', 'password': 't1_pass', 'nickname': 't1_nick', 'vid': 'c_vid1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_set_profile_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'cs1@test.com', 'password': 't1_pass', 'nickname': 'c_nick2', 'vid': 'c_vid1'}
        errorcode4, errormessage4 = customerservice_set_profile_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, nickname has been used.')

        json5 = {'email': 'email_not_exist@a.com', 'password': 't1_pass', 'nickname': 't1_nick', 'vid': 'c_vid1'}
        errorcode5, errormessage5 = customerservice_set_profile_check(json5)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email or vid.')

        json6 = {'email': 'cs1@test.com', 'password': 't1_pass', 'nickname': 't1_nick', 'vid': 'vid_not_exist'}
        errorcode6, errormessage6 = customerservice_set_profile_check(json6)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, wrong email or vid.')

        instance = CustomerService.objects.get(id=2)
        instance.vid_createtime = timezone.now() - timezone.timedelta(days=3)
        instance.save()
        json7 = {'email': 'cs2@test.com', 'password': 't2_pass', 'nickname': 't2_nick', 'vid': 'c_vid2'}
        errorcode7, errormessage7 = customerservice_set_profile_check(json7)
        self.assertEqual(errorcode7, 0)
        self.assertEqual(errormessage7, 'ERROR, vid is expired.')


class TestCsSetProfileCheckVidCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=False, is_online=False, connection_num=0, vid='c_vid2')

    def test(self):
        json1 = {'email': 'cs1@test.com', 'vid': 'c_vid1'}
        errorcode1, errormessage1 = customerservice_set_profile_check_vid_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'cs1@test.com'}
        errorcode2, errormessage2 = customerservice_set_profile_check_vid_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@test.com', 'vid': 'c_vid1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_set_profile_check_vid_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'cs2@test.com', 'vid': 'c_vid1'}
        errorcode4, errormessage4 = customerservice_set_profile_check_vid_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email or vid.')

        json5 = {'email': 'cs1@test.com', 'vid': 'c_vid2'}
        errorcode5, errormessage5 = customerservice_set_profile_check_vid_check(json5)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email or vid.')

        instance = CustomerService.objects.get(id=2)
        instance.vid_createtime = timezone.now() - timezone.timedelta(days=3)
        instance.save()
        json6 = {'email': 'cs2@test.com', 'vid': 'c_vid2'}
        errorcode6, errormessage6 = customerservice_set_profile_check_vid_check(json6)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, vid is expired.')


class TestCsLoginCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        json1 = {'email': 'cs1@test.com', 'password': 'c_pass1'}
        errorcode1, errormessage1 = customerservice_login_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'cs1@test.com'}
        errorcode2, errormessage2 = customerservice_login_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@test.com', 'password': 'c_pass1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_login_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')


class TestCsResetPasswordCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        json1 = {'password': 'c_pass1', 'newpassword': 'Cnewpass1'}
        errorcode1, errormessage1 = customerservice_reset_password_check(json1, c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'password': 'c_pass1'}
        errorcode2, errormessage2 = customerservice_reset_password_check(json2, c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'password': 'c_pass1', 'newpassword': 'Cnewpass1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_reset_password_check(json3, c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        session.delete()
        json4 = {'password': 'c_pass1', 'newpassword': 'Cnewpass1'}
        errorcode4, errormessage4 = customerservice_reset_password_check(json4, c)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, session is broken.')

        c1 = Client()
        session1 = c1.session
        session1['c_email'] = 'cs2@test.com'
        session1.save()
        json5 = {'password': 'c_pass1', 'newpassword': 'Cnewpass1'}
        errorcode5, errormessage5 = customerservice_reset_password_check(json5, c1)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email.')


class TestCsForgetPasswordEmailRequestCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        json1 = {'email': 'cs1@test.com'}
        errorcode1, errormessage1 = customerservice_forget_password_email_request_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {}
        errorcode2, errormessage2 = customerservice_forget_password_email_request_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@test.com', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_forget_password_email_request_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'cs2@test.com'}
        errorcode4, errormessage4 = customerservice_forget_password_email_request_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email.')


class TestCsForgetPasswordCheckVidCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=False, is_online=False, connection_num=0, vid='c_vid2')

    def test(self):
        json1 = {'email': 'cs1@test.com', 'vid': 'c_vid1'}
        errorcode1, errormessage1 = customerservice_forget_password_check_vid_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'cs1@test.com'}
        errorcode2, errormessage2 = customerservice_forget_password_check_vid_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@test.com', 'vid': 'c_vid1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_forget_password_check_vid_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'cs2@test.com', 'vid': 'c_vid1'}
        errorcode4, errormessage4 = customerservice_forget_password_check_vid_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email or vid.')

        json5 = {'email': 'cs1@test.com', 'vid': 'c_vid2'}
        errorcode5, errormessage5 = customerservice_forget_password_check_vid_check(json5)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email or vid.')

        instance = CustomerService.objects.get(id=2)
        instance.vid_createtime = timezone.now() - timezone.timedelta(days=3)
        instance.save()
        json7 = {'email': 'cs2@test.com', 'vid': 'c_vid2'}
        errorcode7, errormessage7 = customerservice_forget_password_check_vid_check(json7)
        self.assertEqual(errorcode7, 0)
        self.assertEqual(errormessage7, 'ERROR, vid is expired.')


class TestCsForgetPasswordSaveDataCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=False, is_online=False, connection_num=0, vid='c_vid2')

    def test(self):
        json1 = {'email': 'cs1@test.com', 'newpassword': 'Cnewpass1', 'vid': 'c_vid1'}
        errorcode1, errormessage1 = customerservice_forget_password_save_data_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'cs1@test.com', 'vid': 'c_vid1'}
        errorcode2, errormessage2 = customerservice_forget_password_save_data_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@test.com', 'newpassword': 'Cnewpass1', 'vid': 'c_vid1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_forget_password_save_data_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'cs2@test.com', 'newpassword': 'Cnewpass1', 'vid': 'c_vid1'}
        errorcode4, errormessage4 = customerservice_forget_password_save_data_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email or vid.')

        json5 = {'email': 'cs1@test.com', 'newpassword': 'Cnewpass1', 'vid': 'c_vid2'}
        errorcode5, errormessage5 = customerservice_forget_password_save_data_check(json5)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email or vid.')

        instance = CustomerService.objects.get(id=2)
        instance.vid_createtime = timezone.now() - timezone.timedelta(days=3)
        instance.save()
        json7 = {'email': 'cs2@test.com', 'newpassword': 'Cnewpass2', 'vid': 'c_vid2'}
        errorcode7, errormessage7 = customerservice_forget_password_save_data_check(json7)
        self.assertEqual(errorcode7, 0)
        self.assertEqual(errormessage7, 'ERROR, vid is expired.')


class TestCsShowUserStatusCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        errorcode1, errormessage1 = customerservice_show_user_status_check(c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        session['c_email'] = 'cs2@test.com'
        session.save()
        errorcode2, errormessage2 = customerservice_show_user_status_check(c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        session.delete()
        errorcode3, errormessage3 = customerservice_show_user_status_check(c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')


class TestCsUpdateConnectionNumCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        json1 = {'connection_num': 10}
        errorcode1, errormessage1 = customerservice_update_connection_num_check(json1, c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {}
        errorcode2, errormessage2 = customerservice_update_connection_num_check(json2, c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'connection_num': 10, 'other': 'other'}
        errorcode3, errormessage3 = customerservice_update_connection_num_check(json3, c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'connection_num': '10'}
        errorcode4, errormessage4 = customerservice_update_connection_num_check(json4, c)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong type.')

        session['c_email'] = 'cs2@test.com'
        session.save()
        json5 = {'connection_num': 10}
        errorcode5, errormessage5 = customerservice_update_connection_num_check(json5, c)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email.')

        session.delete()
        json6 = {'connection_num': 10}
        errorcode6, errormessage6 = customerservice_update_connection_num_check(json6, c)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, session is broken.')


class TestCsUpdateLoginStatusCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        json1 = {'login_status': True}
        errorcode1, errormessage1 = customerservice_update_login_status_check(json1, c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {}
        errorcode2, errormessage2 = customerservice_update_login_status_check(json2, c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'login_status': True, 'other': 'other'}
        errorcode3, errormessage3 = customerservice_update_login_status_check(json3, c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'login_status': 'True'}
        errorcode4, errormessage4 = customerservice_update_login_status_check(json4, c)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong type.')

        session['c_email'] = 'cs2@test.com'
        session.save()
        json5 = {'login_status': True}
        errorcode5, errormessage5 = customerservice_update_login_status_check(json5, c)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email.')

        session.delete()
        json6 = {'login_status': True}
        errorcode6, errormessage6 = customerservice_update_login_status_check(json6, c)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, session is broken.')


class TestCsRobotinfoCreateCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        RobotInfo.objects.create(id=1, enterprise=admin_instance, question='question2', answer='answer2', keyword='keyword2', weight=0)

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        json1 = {'question': 'question1', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0}
        errorcode1, errormessage1 = customerservice_setrobotinfo_create_check(json1, c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'question': 'question1', 'answer': 'answer1', 'weight': 0}
        errorcode2, errormessage2 = customerservice_setrobotinfo_create_check(json2, c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'question': 'question1', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0, 'other': 'other'}
        errorcode3, errormessage3 = customerservice_setrobotinfo_create_check(json3, c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'question': 'question2', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0}
        errorcode4, errormessage4 = customerservice_setrobotinfo_create_check(json4, c)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, info is exist.')

        session['c_email'] = 'cs2@test.com'
        session.save()
        json5 = {'question': 'question3', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0}
        errorcode5, errormessage5 = customerservice_setrobotinfo_create_check(json5, c)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email.')

        session.delete()
        json6 = {'question': 'question3', 'answer': 'answer1', 'keyword': 'keyword1', 'weight': 0}
        errorcode6, errormessage6 = customerservice_setrobotinfo_create_check(json6, c)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, session is broken.')


class TestCsRobotinfoDeleteCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        RobotInfo.objects.create(id=1, enterprise=admin_instance, question='question1', answer='answer1', keyword='keyword1', weight=0)

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        json1 = {'question': 'question1'}
        errorcode1, errormessage1 = customerservice_setrobotinfo_delete_check(json1, c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {}
        errorcode2, errormessage2 = customerservice_setrobotinfo_delete_check(json2, c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'question': 'question1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_setrobotinfo_delete_check(json3, c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'question': 'question2'}
        errorcode4, errormessage4 = customerservice_setrobotinfo_delete_check(json4, c)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, info is not exist.')

        session['c_email'] = 'cs2@test.com'
        session.save()
        json5 = {'question': 'question1'}
        errorcode5, errormessage5 = customerservice_setrobotinfo_delete_check(json5, c)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email.')

        session.delete()
        json6 = {'question': 'question1'}
        errorcode6, errormessage6 = customerservice_setrobotinfo_delete_check(json6, c)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, session is broken.')


class TestCsRobotinfoShowCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        RobotInfo.objects.create(id=1, enterprise=admin_instance, question='question1', answer='answer1', keyword='keyword1', weight=0)

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        errorcode1, errormessage1 = customerservice_setrobotinfo_show_check(c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        session['c_email'] = 'cs2@test.com'
        session.save()
        errorcode2, errormessage2 = customerservice_setrobotinfo_show_check(c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        session.delete()
        errorcode3, errormessage3 = customerservice_setrobotinfo_show_check(c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')


class TestCsDisplayrobotreplyShowCheck(TestCase):
    def test(self):
        json1 = {'nickname': 'a_nick1', 'customer_input': 'nihao'}
        errorcode1, errormessage1 = customerservice_displayrobotreply_show_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'nickname': 'a_nick1'}
        errorcode2, errormessage2 = customerservice_displayrobotreply_show_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'nickname': 'a_nick1', 'customer_input': 'nihao', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_displayrobotreply_show_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')


class TestCsLogoutCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@test.com'
        session.save()

        errorcode1, errormessage1 = customerservice_logout_check(c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        session['c_email'] = 'cs2@test.com'
        session.save()
        errorcode2, errormessage2 = customerservice_logout_check(c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        session.delete()
        errorcode3, errormessage3 = customerservice_logout_check(c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')


class TestCustomerCheckInfoCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        json1 = {'enterprise_id': 'a_nick1', 'customer_id': 'customer1', 'cusotmer_name': 'cusotmerName1', 'hash_result': 'hash1'}
        errorcode1, errormessage1 = customer_check_info_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'enterprise_id': 'a_nick1', 'customer_id': 'customer1', 'cusotmer_name': 'cusotmerName1'}
        errorcode2, errormessage2 = customer_check_info_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'enterprise_id': 'a_nick1', 'customer_id': 'customer1', 'cusotmer_name': 'cusotmerName1', 'hash_result': 'hash1', 'other': 'other'}
        errorcode3, errormessage3 = customer_check_info_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'enterprise_id': 'a_nick2', 'customer_id': 'customer1', 'cusotmer_name': 'cusotmerName1', 'hash_result': 'hash1'}
        errorcode4, errormessage4 = customer_check_info_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong nickname.')


class TestCustomerDisplayCustomerInfoPropertyNameCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@test.com', nickname='a_nick1', password='a_pass1', web_url='a_weburl1', widget_url='a_widgeturl1', mobile_url='a_mobileurl1', communication_key='a_key1', vid='a_vid1')

    def test(self):
        json1 = {'enterprise_id': 'a_nick1'}
        errorcode1, errormessage1 = customer_display_customerinfopropertyname_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {}
        errorcode2, errormessage2 = customer_display_customerinfopropertyname_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'enterprise_id': 'a_nick1', 'other': 'other'}
        errorcode3, errormessage3 = customer_display_customerinfopropertyname_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'enterprise_id': 'a_nick2'}
        errorcode4, errormessage4 = customer_display_customerinfopropertyname_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong nickname.')
