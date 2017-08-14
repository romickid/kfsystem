from django.test import TestCase
from .robot import *
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