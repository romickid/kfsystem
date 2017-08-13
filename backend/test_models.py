from django.test import TestCase
from django.test import Client
from .models import Admin, CustomerService, ChattingLog, SerialNumber, ImageLog, EnterpriseDisplayInfo, RobotInfo


class TestModelAdmin(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        instance = Admin.objects.get(id=1)

        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.email, 'admin1@test.com')
        self.assertEqual(instance.nickname, 'a_nick1')
        self.assertEqual(instance.password, 'a_pass1')
        self.assertEqual(instance.web_url, 'a_weburl1')
        self.assertEqual(instance.widget_url, 'a_weidgeturl1')
        self.assertEqual(instance.mobile_url, 'a_mobileurl1')
        self.assertEqual(instance.communication_key, 'a_key1')
        self.assertEqual(instance.vid, 'a_vid1')


class TestModelCs(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email="cs1@test.com", enterprise=admin_instance, nickname="c_nick1", password="c_pass1", is_register=False, is_online=False, connection_num=0, vid="c_vid1")
        cs_instance = CustomerService.objects.get(id=1)

        self.assertEqual(cs_instance.id, 1)
        self.assertEqual(cs_instance.email, 'cs1@test.com')
        self.assertEqual(cs_instance.enterprise, admin_instance)
        self.assertEqual(cs_instance.nickname, 'c_nick1')
        self.assertEqual(cs_instance.password, 'c_pass1')
        self.assertEqual(cs_instance.is_register, False)
        self.assertEqual(cs_instance.is_online, False)
        self.assertEqual(cs_instance.connection_num, 0)
        self.assertEqual(cs_instance.vid, 'c_vid1')


class TestModelCl(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email="cs1@test.com", enterprise=admin_instance, nickname="c_nick1", password="c_pass1", is_register=False, is_online=False, connection_num=0, vid="c_vid1")
        cs_instance = CustomerService.objects.get(id=1)
        ChattingLog.objects.create(id=1, client_id='cid1', service_id=cs_instance, content='this is content', is_client=False)
        cl_instance = ChattingLog.objects.get(id=1)

        self.assertEqual(cl_instance.id, 1)
        self.assertEqual(cl_instance.client_id, 'cid1')
        self.assertEqual(cl_instance.service_id, cs_instance)
        self.assertEqual(cl_instance.content, 'this is content')
        self.assertEqual(cl_instance.is_client, False)
        # self.assertEqual(cl_instance.time, False)


class TestModelSn(TestCase):
    def test(self):
        SerialNumber.objects.create(id=1, serials='s1', is_used=False)
        sn_instance = SerialNumber.objects.get(id=1)

        self.assertEqual(sn_instance.id, 1)
        self.assertEqual(sn_instance.serials, 's1')
        self.assertEqual(sn_instance.is_used, False)


class TestModelImagelog(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email="cs1@test.com", enterprise=admin_instance, nickname="c_nick1", password="c_pass1", is_register=False, is_online=False, connection_num=0, vid="c_vid1")
        cs_instance = CustomerService.objects.get(id=1)
        ImageLog.objects.create(id=1, client_id='cid1', service_id=cs_instance, is_client=False)
        image_instance = ImageLog.objects.get(id=1)

        self.assertEqual(image_instance.id, 1)
        self.assertEqual(image_instance.client_id, 'cid1')
        self.assertEqual(image_instance.service_id, cs_instance)
        self.assertEqual(image_instance.is_client, False)


class TestModelEnterpriseDisplayInfo(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        EnterpriseDisplayInfo.objects.create(id=1, enterprise=admin_instance, name="info1", comment="this is info1")
        displayinfo_instance = EnterpriseDisplayInfo.objects.get(id=1)

        self.assertEqual(displayinfo_instance.id, 1)
        self.assertEqual(displayinfo_instance.enterprise, admin_instance)
        self.assertEqual(displayinfo_instance.name, "info1")
        self.assertEqual(displayinfo_instance.comment, "this is info1")


class TestModelRobotInfo(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        RobotInfo.objects.create(id=1, enterprise=admin_instance, question="question1", answer="this is answer1", keyword='keyword1', weight=0)
        robotinfo_instance = RobotInfo.objects.get(id=1)

        self.assertEqual(robotinfo_instance.id, 1)
        self.assertEqual(robotinfo_instance.enterprise, admin_instance)
        self.assertEqual(robotinfo_instance.question, "question1")
        self.assertEqual(robotinfo_instance.answer, "this is answer1")
        self.assertEqual(robotinfo_instance.keyword, "keyword1")
        self.assertEqual(robotinfo_instance.weight, 0)
