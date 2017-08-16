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


def robot_add_keyword(keyword):
    jieba.add_word(keyword)


def robot_weight_list(admin_id, customer_input):
    instance_robotinfo = RobotInfo.objects.filter(enterprise=admin_id)
    array_input_tags = robot_create_tags(customer_input)
    weight_list = list()
    for i in instance_robotinfo:
        dict_questions_tags = robot_create_tags_withWeight(i.question)
        weight = robot_similarity(array_input_tags, dict_questions_tags) * i.weight
        weight_list.append([weight, i.question, i.answer])
    return weight_list


def robot_return_answer(admin_id, customer_input):
    weight_robot = robot_weight_list(admin_id, customer_input)
    weight_robot.sort(reverse=True)
    weight_basic = robot_basic_weight_list(customer_input)
    weight_basic.sort(reverse=True)
    if weight_robot[0][0] > 5:
        return weight_robot[0]
    elif weight_basic[0][0] > 3:
        return weight_basic[0]
    else:
        return ['NO Reply.']
