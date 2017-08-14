import jieba.analyse
from .models import Admin, RobotInfo
from .serializers import AdminSerializer, RobotInfoSerializer


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
        weight_list.append([weight, i.question, i.answer, i.keyword])
    return weight_list


def robot_return_answer(admin_id, customer_input, max_answer_num=5):
    weight_list = robot_weight_list(admin_id, customer_input)
    weight_list.sort(reverse=True)
    if len(weight_list) > max_answer_num:
        return weight_list[0:max_answer_num]
    else:
        return weight_list
