from django.test import TestCase
from django.test.client import Client
from .views_helper_functions import *
from .views_check_functions import *
from .models import Admin, CustomerService, ChattingLog, SerialNumber, ImageLog, EnterpriseDisplayInfo


class TestAdminCreateCheck(TestCase):
    def setUp(self):
        SerialNumber.objects.create(serials='s1', is_used=False)
        SerialNumber.objects.create(serials='s2', is_used=False)
        SerialNumber.objects.create(serials='s3', is_used=False)
        SerialNumber.objects.create(serials='s4', is_used=True)
        SerialNumber.objects.create(serials='s5', is_used=False)
        SerialNumber.objects.create(serials='s6', is_used=False)
        SerialNumber.objects.create(serials='s7', is_used=False)
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

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

        json5 = {'email': 'admin1@a.com', 'nickname': 'nick5', 'password': 'pass5', 'serials': 's5'}
        errorcode5, errormessage5 = admin_create_check(json5)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, email has been registered.')

        json6 = {'email': 'cs1@a.com', 'nickname': 'nick6', 'password': 'pass6', 'serials': 's6'}
        errorcode6, errormessage6 = admin_create_check(json6)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, email has been registered.')

        json7 = {'email': 'test7@a.com', 'nickname': 'Anick1', 'password': 'pass7', 'serials': 's7'}
        errorcode7, errormessage7 = admin_create_check(json7)
        self.assertEqual(errorcode7, 0)
        self.assertEqual(errormessage7, 'ERROR, nickname has been used.')


class TestAdminLoginCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')

    def test(self):
        json1 = {'email': 'admin1@a.com', 'password': 'Apass1'}
        errorcode1, errormessage1 = admin_login_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'admin1@a.com'}
        errorcode2, errormessage2 = admin_login_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'admin1@a.com', 'nickname': 'nick3', 'password': 'Apass1'}
        errorcode3, errormessage3 = admin_login_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')


class TestAdminResetPasswordCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@a.com'
        session.save()

        json1 = {'password': 'Apass1', 'newpassword': 'Anewpass1'}
        errorcode1, errormessage1 = admin_reset_password_check(json1, c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'password': 'Apass1'}
        errorcode2, errormessage2 = admin_reset_password_check(json2, c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'password': 'Apass1', 'newpassword': 'Anewpass1', 'other': 'other'}
        errorcode3, errormessage3 = admin_reset_password_check(json3, c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'password': 'Apass1', 'newpassword': 'Anewpass1'}
        session['a_email'] = 'admin2@a.com'
        session.save()
        errorcode4, errormessage4 = admin_reset_password_check(json4, c)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email.')

        json5 = {'password': 'Apass1', 'newpassword': 'Anewpass1'}
        session.delete()
        errorcode5, errormessage5 = admin_reset_password_check(json5, c)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, session is broken.')


class TestAdminForgetPasswordEmailRequestCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')

    def test(self):
        json1 = {'email': 'admin1@a.com'}
        errorcode1, errormessage1 = admin_forget_password_email_request_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {}
        errorcode2, errormessage2 = admin_forget_password_email_request_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'admin1@a.com', 'password': 'Apass1'}
        errorcode3, errormessage3 = admin_forget_password_email_request_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'admin2@a.com'}
        errorcode4, errormessage4 = admin_forget_password_email_request_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email.')


class TestAdminForgetPasswordCheckVidCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')

    def test(self):
        json1 = {'email': 'admin1@a.com', 'vid': 'Avid1'}
        errorcode1, errormessage1 = admin_forget_password_check_vid_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'admin1@a.com'}
        errorcode2, errormessage2 = admin_forget_password_check_vid_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'admin1@a.com', 'password': 'Apass1', 'vid': 'Avid1'}
        errorcode3, errormessage3 = admin_forget_password_check_vid_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'admin2@a.com', 'vid': 'Avid1'}
        errorcode4, errormessage4 = admin_forget_password_check_vid_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email or vid.')

        json5 = {'email': 'admin1@a.com', 'vid': 'vid1'}
        errorcode5, errormessage5 = admin_forget_password_check_vid_check(json5)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email or vid.')


class TestAdminForgetPasswordSaveDataCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')

    def test(self):
        json1 = {'email': 'admin1@a.com', 'newpassword': 'Anewpass1'}
        errorcode1, errormessage1 = admin_forget_password_save_data_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'admin1@a.com'}
        errorcode2, errormessage2 = admin_forget_password_save_data_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'admin1@a.com', 'password': 'Apass1', 'newpassword': 'Anewpass1'}
        errorcode3, errormessage3 = admin_forget_password_save_data_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'admin2@a.com', 'newpassword': 'Anewpass1'}
        errorcode4, errormessage4 = admin_forget_password_save_data_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email.')


class TestAdminShowCommunicationKeyCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@a.com'
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


class TestAdminResetCommunicationKeyCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@a.com'
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


class TestAdminShowCsStatusCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@a.com'
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


class TestAdminShowUserStatusCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@a.com'
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


class TestAdminDisplayInfoCreateCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        instance = Admin.objects.get(id=1)
        EnterpriseDisplayInfo.objects.create(id=1, enterprise=instance, name='id_used', comment='this is id')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@a.com'
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
        session1['a_email'] = 'admin1@a.com'
        session1.save()
        json4 = {'name': 'id_used', 'comment': 'this is id'}
        errorcode4, errormessage4 = admin_display_info_create_check(json4, c1)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, attribute name has been used.')


class TestAdminDisplayInfoDeleteCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        instance = Admin.objects.get(id=1)
        EnterpriseDisplayInfo.objects.create(id=1, enterprise=instance, name='id_used', comment='this is id')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@a.com'
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
        session1['a_email'] = 'admin1@a.com'
        session1.save()
        json4 = {'name': 'id'}
        errorcode4, errormessage4 = admin_display_info_delete_check(json4, c1)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, attribute is not existent.')


class TestAdminDisplayInfoShowCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        Admin.objects.create(id=2, email='admin2@a.com', nickname='Anick2', password='Apass2', web_url='Aweb_url2', widget_url='Awidget_url2', mobile_url='Amobile_url2', communication_key='Akey2', vid='Avid2')
        instance = Admin.objects.get(id=1)
        EnterpriseDisplayInfo.objects.create(id=1, enterprise=instance, name='id_used', comment='this is id')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@a.com'
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


class TestCsCreateCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

    def test(self):
        c = Client()
        session = c.session
        session['a_email'] = 'admin1@a.com'
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
        session['a_email'] = 'admin1@a.com'
        session.save()

        json6 = {'email': 'cs1@a.com'}
        errorcode6, errormessage6 = customerservice_create_check(json6, c1)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, email has been registered.')

        json7 = {'email': 'admin1@a.com'}
        errorcode7, errormessage7 = customerservice_create_check(json7, c1)
        self.assertEqual(errorcode7, 0)
        self.assertEqual(errormessage7, 'ERROR, email has been registered.')


class TestCsSetProfileCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')
        CustomerService.objects.create(id=2, email='cs2@a.com', enterprise=admin_instance, nickname='Cnick2', password='Cpass2', is_register=False, is_online=False, connection_num=0, vid='Cvid2')

    def test(self):
        json1 = {'email': 'cs1@a.com', 'password': 't1_pass', 'nickname': 't1_nick', 'vid': 'Cvid1'}
        errorcode1, errormessage1 = customerservice_set_profile_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'cs1@a.com', 'password': 't1_pass', 'vid': 'Cvid1'}
        errorcode2, errormessage2 = customerservice_set_profile_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@a.com', 'password': 't1_pass', 'nickname': 't1_nick', 'vid': 'Cvid1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_set_profile_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'cs1@a.com', 'password': 't1_pass', 'nickname': 'Cnick2', 'vid': 'Cvid1'}
        errorcode4, errormessage4 = customerservice_set_profile_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, nickname has been used.')

        json5 = {'email': 'email_not_exist@a.com', 'password': 't1_pass', 'nickname': 't1_nick', 'vid': 'Cvid1'}
        errorcode5, errormessage5 = customerservice_set_profile_check(json5)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email or vid.')

        json6 = {'email': 'cs1@a.com', 'password': 't1_pass', 'nickname': 't1_nick', 'vid': 'vid_not_exist'}
        errorcode6, errormessage6 = customerservice_set_profile_check(json6)
        self.assertEqual(errorcode6, 0)
        self.assertEqual(errormessage6, 'ERROR, wrong email or vid.')


class TestCsSetProfileCheckVidCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

    def test(self):
        json1 = {'email': 'cs1@a.com', 'vid': 'Cvid1'}
        errorcode1, errormessage1 = customerservice_set_profile_check_vid_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'cs1@a.com'}
        errorcode2, errormessage2 = customerservice_set_profile_check_vid_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@a.com', 'vid': 'Cvid1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_set_profile_check_vid_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'cs2@a.com', 'vid': 'Cvid1'}
        errorcode4, errormessage4 = customerservice_set_profile_check_vid_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email or vid.')

        json5 = {'email': 'cs1@a.com', 'vid': 'Cvid2'}
        errorcode5, errormessage5 = customerservice_set_profile_check_vid_check(json5)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email or vid.')


class TestCsLoginCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

    def test(self):
        json1 = {'email': 'cs1@a.com', 'password': 'Cpass1'}
        errorcode1, errormessage1 = customerservice_login_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'cs1@a.com'}
        errorcode2, errormessage2 = customerservice_login_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@a.com', 'password': 'Cpass1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_login_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')


class TestCsResetPasswordCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@a.com'
        session.save()

        json1 = {'password': 'Cpass1', 'newpassword': 'Cnewpass1'}
        errorcode1, errormessage1 = customerservice_reset_password_check(json1, c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'password': 'Cpass1'}
        errorcode2, errormessage2 = customerservice_reset_password_check(json2, c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'password': 'Cpass1', 'newpassword': 'Cnewpass1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_reset_password_check(json3, c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        session.delete()
        json4 = {'password': 'Cpass1', 'newpassword': 'Cnewpass1'}
        errorcode4, errormessage4 = customerservice_reset_password_check(json4, c)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, session is broken.')

        c1 = Client()
        session1 = c1.session
        session1['c_email'] = 'cs2@a.com'
        session1.save()
        json5 = {'password': 'Cpass1', 'newpassword': 'Cnewpass1'}
        errorcode5, errormessage5 = customerservice_reset_password_check(json5, c1)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email.')


class TestCsForgetPasswordEmailRequestCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

    def test(self):
        json1 = {'email': 'cs1@a.com'}
        errorcode1, errormessage1 = customerservice_forget_password_email_request_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {}
        errorcode2, errormessage2 = customerservice_forget_password_email_request_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@a.com', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_forget_password_email_request_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'cs2@a.com'}
        errorcode4, errormessage4 = customerservice_forget_password_email_request_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email.')


class TestCsForgetPasswordCheckVidCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

    def test(self):
        json1 = {'email': 'cs1@a.com', 'vid': 'Cvid1'}
        errorcode1, errormessage1 = customerservice_forget_password_check_vid_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'cs1@a.com'}
        errorcode2, errormessage2 = customerservice_forget_password_check_vid_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@a.com', 'vid': 'Cvid1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_forget_password_check_vid_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'cs2@a.com', 'vid': 'Cvid1'}
        errorcode4, errormessage4 = customerservice_forget_password_check_vid_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email or vid.')

        json4 = {'email': 'cs1@a.com', 'vid': 'Cvid2'}
        errorcode4, errormessage4 = customerservice_forget_password_check_vid_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email or vid.')


class TestCsForgetPasswordSaveDataCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

    def test(self):
        json1 = {'email': 'cs1@a.com', 'newpassword': 'Cnewpass1', 'vid': 'Cvid1'}
        errorcode1, errormessage1 = customerservice_forget_password_save_data_check(json1)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        json2 = {'email': 'cs1@a.com', 'vid': 'Cvid1'}
        errorcode2, errormessage2 = customerservice_forget_password_save_data_check(json2)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, incomplete information.')

        json3 = {'email': 'cs1@a.com', 'newpassword': 'Cnewpass1', 'vid': 'Cvid1', 'other': 'other'}
        errorcode3, errormessage3 = customerservice_forget_password_save_data_check(json3)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, wrong information.')

        json4 = {'email': 'cs2@a.com', 'newpassword': 'Cnewpass1', 'vid': 'Cvid1'}
        errorcode4, errormessage4 = customerservice_forget_password_save_data_check(json4)
        self.assertEqual(errorcode4, 0)
        self.assertEqual(errormessage4, 'ERROR, wrong email or vid.')

        json5 = {'email': 'cs1@a.com', 'newpassword': 'Cnewpass1', 'vid': 'Cvid2'}
        errorcode5, errormessage5 = customerservice_forget_password_save_data_check(json5)
        self.assertEqual(errorcode5, 0)
        self.assertEqual(errormessage5, 'ERROR, wrong email or vid.')


class TestCsShowUserStatusCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@a.com'
        session.save()

        errorcode1, errormessage1 = customerservice_show_user_status_check(c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        session['c_email'] = 'cs2@a.com'
        session.save()
        errorcode2, errormessage2 = customerservice_show_user_status_check(c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        session.delete()
        errorcode3, errormessage3 = customerservice_show_user_status_check(c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')


class TestCsLogoutCheck(TestCase):
    def setUp(self):
        Admin.objects.create(id=1, email='admin1@a.com', nickname='Anick1', password='Apass1', web_url='Aweb_url1', widget_url='Awidget_url1', mobile_url='Amobile_url1', communication_key='Akey1', vid='Avid1')
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email='cs1@a.com', enterprise=admin_instance, nickname='Cnick1', password='Cpass1', is_register=False, is_online=False, connection_num=0, vid='Cvid1')

    def test(self):
        c = Client()
        session = c.session
        session['c_email'] = 'cs1@a.com'
        session.save()

        errorcode1, errormessage1 = customerservice_logout_check(c)
        self.assertEqual(errorcode1, 1)
        self.assertEqual(errormessage1, 'No ERROR.')

        session['c_email'] = 'cs2@a.com'
        session.save()
        errorcode2, errormessage2 = customerservice_logout_check(c)
        self.assertEqual(errorcode2, 0)
        self.assertEqual(errormessage2, 'ERROR, wrong email.')

        session.delete()
        errorcode3, errormessage3 = customerservice_logout_check(c)
        self.assertEqual(errorcode3, 0)
        self.assertEqual(errormessage3, 'ERROR, session is broken.')

