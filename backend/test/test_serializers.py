from django.test import TestCase
from ..models import Admin, CustomerService, ChattingLog, SerialNumber, ImageLog, EnterpriseDisplayInfo, RobotInfo
from ..serializers import AdminSerializer, CustomerServiceSerializer, CustomerServiceCreateSerializer, ChattingLogSerializer, SerialNumberSerializer, ImageLogSerializer, EnterpriseDisplayInfoSerializer, RobotInfoSerializer
from django.utils import timezone


class TestAdminSerializer(TestCase):
    def test(self):
        json_create = dict()
        json_create['email'] = 'admin1@test.com'
        json_create['nickname'] = 'a_nick1'
        json_create['password'] = 'a_pass1'
        json_create['web_url'] = "a_weburl1"
        json_create['widget_url'] = "a_widgeturl1"
        json_create['mobile_url'] = "a_mobileurl1"
        json_create['communication_key'] = 'a_key1'
        json_create['vid'] = 'a_vid1'
        json_create['vid_createtime'] = timezone.now()

        serializer = AdminSerializer(data=json_create)
        if serializer.is_valid():
            serializer.save()
        instance = Admin.objects.get(email=json_create['email'])

        self.assertEqual(instance.email, 'admin1@test.com')
        self.assertEqual(instance.nickname, 'a_nick1')
        self.assertEqual(instance.password, 'a_pass1')
        self.assertEqual(instance.web_url, 'a_weburl1')
        self.assertEqual(instance.widget_url, 'a_widgeturl1')
        self.assertEqual(instance.mobile_url, 'a_mobileurl1')
        self.assertEqual(instance.communication_key, 'a_key1')
        self.assertEqual(instance.vid, 'a_vid1')


class TestCustomerServiceCreateSerializer(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)

        json_create = dict()
        json_create['email'] = 'cs1@test.com'
        json_create['enterprise'] = 1
        json_create['nickname'] = 'c_nick1'
        json_create['password'] = 'c_pass1'
        json_create['is_register'] = False
        json_create['is_online'] = False
        json_create['connection_num'] = 0
        json_create['vid'] = 'c_vid1'
        json_create['vid_createtime'] = timezone.now()

        serializer = CustomerServiceCreateSerializer(data=json_create)
        if serializer.is_valid():
            serializer.save()
        instance = CustomerService.objects.get(email=json_create['email'])

        self.assertEqual(instance.email, 'cs1@test.com')
        self.assertEqual(instance.enterprise, admin_instance)
        self.assertEqual(instance.nickname, 'c_nick1')
        self.assertEqual(instance.password, 'c_pass1')
        self.assertEqual(instance.is_register, False)
        self.assertEqual(instance.is_online, False)
        self.assertEqual(instance.connection_num, 0)
        self.assertEqual(instance.vid, 'c_vid1')


class TestCustomerServiceSerializer(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email="cs1@test.com", enterprise=admin_instance, nickname="c_nick1", password="c_pass1", is_register=False, is_online=False, connection_num=0, vid="c_vid1")

        json_modify = dict()
        json_modify['email'] = 'cs2@test.com'
        json_modify['enterprise'] = 1
        json_modify['nickname'] = 'c_nick2'
        json_modify['password'] = 'c_pass2'
        json_modify['is_register'] = True
        json_modify['is_online'] = True
        json_modify['connection_num'] = 1
        json_modify['vid'] = 'c_vid2'
        json_modify['vid_createtime'] = timezone.now()

        instance = CustomerService.objects.get(id=1)
        serializer = CustomerServiceSerializer(instance, data=json_modify)
        if serializer.is_valid():
            serializer.save()

        self.assertEqual(instance.email, 'cs2@test.com')
        self.assertEqual(instance.enterprise, admin_instance)
        self.assertEqual(instance.nickname, 'c_nick2')
        self.assertEqual(instance.password, 'c_pass2')
        self.assertEqual(instance.is_register, True)
        self.assertEqual(instance.is_online, True)
        self.assertEqual(instance.connection_num, 1)
        self.assertEqual(instance.vid, 'c_vid2')


class TestChattingLogSerializer(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email="cs1@test.com", enterprise=admin_instance, nickname="c_nick1", password="c_pass1", is_register=False, is_online=False, connection_num=0, vid="c_vid1")
        CustomerService.objects.create(id=2, email="cs2@test.com", enterprise=admin_instance, nickname="c_nick2", password="c_pass2", is_register=False, is_online=False, connection_num=0, vid="c_vid2")
        cs_instance1 = CustomerService.objects.get(id=1)
        cs_instance2 = CustomerService.objects.get(id=2)

        json_create = dict()
        json_create['client_id'] = 'cid1'
        json_create['service_id'] = 1
        json_create['content'] = 'this is content1'
        json_create['is_client'] = False

        serializer = ChattingLogSerializer(data=json_create)
        if serializer.is_valid():
            serializer.save()
        instance = ChattingLog.objects.get(client_id='cid1')
        instance_id = instance.id
        self.assertEqual(instance.client_id, 'cid1')
        self.assertEqual(instance.service_id, cs_instance1)
        self.assertEqual(instance.content, 'this is content1')
        self.assertEqual(instance.is_client, False)

        json_modify = dict()
        json_modify['client_id'] = 'cid2'
        json_modify['service_id'] = 2
        json_modify['content'] = 'this is content2'
        json_modify['is_client'] = True

        instance = ChattingLog.objects.get(id=instance_id)
        serializer = ChattingLogSerializer(instance, data=json_modify)
        if serializer.is_valid():
            serializer.save()
        self.assertEqual(instance.client_id, 'cid2')
        self.assertEqual(instance.service_id, cs_instance2)
        self.assertEqual(instance.content, 'this is content2')
        self.assertEqual(instance.is_client, True)


class TestSerialNumberSerializer(TestCase):
    def test(self):
        json_create = dict()
        json_create['serials'] = 's1'
        json_create['is_used'] = False

        serializer = SerialNumberSerializer(data=json_create)
        if serializer.is_valid():
            serializer.save()
        instance = SerialNumber.objects.get(serials='s1')
        instance_id = instance.id
        self.assertEqual(instance.serials, 's1')
        self.assertEqual(instance.is_used, False)

        json_modify = dict()
        json_modify['serials'] = 's2'
        json_modify['is_used'] = True

        instance = SerialNumber.objects.get(id=instance_id)
        serializer = SerialNumberSerializer(instance, data=json_modify)
        if serializer.is_valid():
            serializer.save()
        self.assertEqual(instance.serials, 's2')
        self.assertEqual(instance.is_used, True)


class TestImageLogSerializer(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        CustomerService.objects.create(id=1, email="cs1@test.com", enterprise=admin_instance, nickname="c_nick1", password="c_pass1", is_register=False, is_online=False, connection_num=0, vid="c_vid1")
        CustomerService.objects.create(id=2, email="cs2@test.com", enterprise=admin_instance, nickname="c_nick2", password="c_pass2", is_register=False, is_online=False, connection_num=0, vid="c_vid2")
        cs_instance1 = CustomerService.objects.get(id=1)
        cs_instance2 = CustomerService.objects.get(id=2)

        json_create = dict()
        json_create['client_id'] = 'cid1'
        json_create['service_id'] = 1
        json_create['is_client'] = False

        serializer = ImageLogSerializer(data=json_create)
        if serializer.is_valid():
            serializer.save()
        instance = ImageLog.objects.get(client_id='cid1')
        instance_id = instance.id
        self.assertEqual(instance.client_id, 'cid1')
        self.assertEqual(instance.service_id, cs_instance1)
        self.assertEqual(instance.is_client, False)

        json_modify = dict()
        json_modify['client_id'] = 'cid2'
        json_modify['service_id'] = 2
        json_modify['is_client'] = True

        instance = ImageLog.objects.get(id=instance_id)
        serializer = ImageLogSerializer(instance, data=json_modify)
        if serializer.is_valid():
            serializer.save()
        self.assertEqual(instance.client_id, 'cid2')
        self.assertEqual(instance.service_id, cs_instance2)
        self.assertEqual(instance.is_client, True)


class TestEnterpriseDisplayInfoSerializer(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        Admin.objects.create(id=2, email="admin2@test.com", nickname="a_nick2", password="a_pass2", web_url="a_weburl2", widget_url="a_weidgeturl2", mobile_url="a_mobileurl2", communication_key="a_key2", vid="a_vid2")
        admin_instance1 = Admin.objects.get(id=1)
        admin_instance2 = Admin.objects.get(id=2)

        json_create = dict()
        json_create['enterprise'] = 1
        json_create['name'] = 'info1'
        json_create['comment'] = 'this is info1'

        serializer = EnterpriseDisplayInfoSerializer(data=json_create)
        if serializer.is_valid():
            serializer.save()
        instance = EnterpriseDisplayInfo.objects.get(name='info1')
        instance_id = instance.id
        self.assertEqual(instance.enterprise, admin_instance1)
        self.assertEqual(instance.name, 'info1')
        self.assertEqual(instance.comment, 'this is info1')

        json_modify = dict()
        json_modify['enterprise'] = 2
        json_modify['name'] = 'info2'
        json_modify['comment'] = 'this is info2'

        instance = EnterpriseDisplayInfo.objects.get(id=instance_id)
        serializer = EnterpriseDisplayInfoSerializer(instance, data=json_modify)
        if serializer.is_valid():
            serializer.save()
        self.assertEqual(instance.enterprise, admin_instance2)
        self.assertEqual(instance.name, 'info2')
        self.assertEqual(instance.comment, 'this is info2')


class TestEnterpriseDisplayInfoSerializer(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        Admin.objects.create(id=2, email="admin2@test.com", nickname="a_nick2", password="a_pass2", web_url="a_weburl2", widget_url="a_weidgeturl2", mobile_url="a_mobileurl2", communication_key="a_key2", vid="a_vid2")
        admin_instance1 = Admin.objects.get(id=1)
        admin_instance2 = Admin.objects.get(id=2)

        json_create = dict()
        json_create['enterprise'] = 1
        json_create['question'] = 'question1'
        json_create['answer'] = 'this is answer1'
        json_create['keyword'] = 'keyword1'
        json_create['weight'] = 0

        serializer = RobotInfoSerializer(data=json_create)
        if serializer.is_valid():
            serializer.save()
        instance = RobotInfo.objects.get(question='question1')
        instance_id = instance.id
        self.assertEqual(instance.enterprise, admin_instance1)
        self.assertEqual(instance.question, "question1")
        self.assertEqual(instance.answer, "this is answer1")
        self.assertEqual(instance.keyword, "keyword1")
        self.assertEqual(instance.weight, 0)

        json_modify = dict()
        json_modify['enterprise'] = 2
        json_modify['question'] = 'question2'
        json_modify['answer'] = 'this is answer2'
        json_modify['keyword'] = 'keyword2'
        json_modify['weight'] = 1

        instance = RobotInfo.objects.get(id=instance_id)
        serializer = RobotInfoSerializer(instance, data=json_modify)
        if serializer.is_valid():
            serializer.save()
        self.assertEqual(instance.enterprise, admin_instance2)
        self.assertEqual(instance.question, "question2")
        self.assertEqual(instance.answer, "this is answer2")
        self.assertEqual(instance.keyword, "keyword2")
        self.assertEqual(instance.weight, 1)
