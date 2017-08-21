#coding:utf-8
import jieba.analyse
from .models import Admin, RobotInfo
from .serializers import AdminSerializer, RobotInfoSerializer
from .robot_basic import *


def robot_create_tags_withWeight(sentence):
    tags = jieba.analyse.extract_tags(sentence, topK=10, withWeight=True)
    return dict(tags)


def robot_create_tags(sentence):
    tags = jieba.analyse.extract_tags(sentence, topK=10, withWeight=False)
    return tags


def robot_similarity(array_input, dict_questions):
    len_input_tags = len(array_input)
    sim_sum = 0
    for i in range(len_input_tags):
       if array_input[i] in dict_questions:
           sim_sum += dict_questions[array_input[i]]
    return sim_sum


def robot_add_keyword(str_keyword):
    list_keyword = str_keyword.split(' ')
    for i in list_keyword:
        jieba.add_word(i)


def robot_weight_list(admin_id, customer_input):
    instance_robotinfo = RobotInfo.objects.filter(enterprise=admin_id)
    if instance_robotinfo.exists() == False:
        return 0
    array_input_tags = robot_create_tags(customer_input)
    weight_list = list()
    for i in instance_robotinfo:
        dict_questions_tags = robot_create_tags_withWeight(i.question)
        weight = robot_similarity(array_input_tags, dict_questions_tags) * i.weight
        weight_list.append([weight, i.question, i.answer])
    return weight_list


def robot_return_answer(admin_id, customer_input):
    weight_robot = robot_weight_list(admin_id, customer_input)
    if weight_robot != 0:
        weight_robot.sort(reverse=True)
    weight_basic = robot_basic_weight_list(customer_input)
    if weight_basic != 0:
        weight_basic.sort(reverse=True)
    if weight_robot != 0 and weight_robot[0][0] > 3:
        return weight_robot[0][1] + '   ' + weight_robot[0][2]
    elif weight_basic != 0 and weight_basic[0][0] > 2:
        return weight_basic[0][1]
    else:
        return ['很抱歉，我不是很清楚您说的是什么，请尝试询问其他问题或使用人工客服。']
