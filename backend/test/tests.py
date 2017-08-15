from django.test import TestCase
from ..robot import *
import time

'''
class TestTemp(TestCase):
    def test(self):
        Admin.objects.create(id=1, email="admin1@test.com", nickname="a_nick1", password="a_pass1", web_url="a_weburl1", widget_url="a_weidgeturl1", mobile_url="a_mobileurl1", communication_key="a_key1", vid="a_vid1")
        admin_instance = Admin.objects.get(id=1)
        RobotInfo.objects.create(id=1, enterprise=admin_instance, question='a1', answer='answer1', keyword='keyword1', weight=1)
        RobotInfo.objects.create(id=2, enterprise=admin_instance, question='a2', answer='answer2', keyword='keyword2', weight=1)
        RobotInfo.objects.create(id=3, enterprise=admin_instance, question='a3', answer='answer3', keyword='keyword3', weight=1)
        RobotInfo.objects.create(id=4, enterprise=admin_instance, question='a4', answer='answer4', keyword='keyword4', weight=1)

        print(robot_return_answer(1, "a1", 3))
        time.sleep(3)
        print(robot_return_answer(1, "a2", 3))
'''

'''
@csrf_exempt
def test_file(request):
    if request.method == 'POST':
        admin_instance = Admin.objects.get(id=1)

        # CustomerService.objects.create(id=1, email='cs1@test.com', enterprise=admin_instance, nickname='c_nick1', password='c_pass1', is_register=False, is_online=False, connection_num=0, vid='c_vid1')
        # CustomerService.objects.create(id=2, email='cs2@test.com', enterprise=admin_instance, nickname='c_nick2', password='c_pass2', is_register=False, is_online=False, connection_num=0, vid='c_vid2')
        # CustomerService.objects.create(id=3, email='cs3@test.com', enterprise=admin_instance, nickname='c_nick3', password='c_pass3', is_register=False, is_online=False, connection_num=0, vid='c_vid3')
        json1 = {'client_id': '1','service_id': '1','content': 'hahaha1','is_client': 1,'time': '2017-08-13 13:33:33'}
        json2 = {'client_id': '1','service_id': '1','content': 'hahaha2','is_client': 1,'time': '2017-08-14 13:33:33'}
        json3 = {'client_id': '1','service_id': '1','content': 'hahaha3','is_client': 1,'time': '2017-08-15 13:33:33'}
        serializer1 = ChattingLogSerializer(data=json1)
        serializer2 = ChattingLogSerializer(data=json2)
        serializer3 = ChattingLogSerializer(data=json3)


        if serializer1.is_valid():
            serializer1.save()
        if serializer2.is_valid():
            serializer2.save()
        if serializer3.is_valid():
            serializer3.save()
        return HttpResponse('OK', status=401)
'''