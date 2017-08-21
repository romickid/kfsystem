from .models import RobotGossipInfo
import jieba


def robot_basic_read():
    list_file = list()
    f = open('./media/basic_corpus.txt','r')
    line = f.readline()
    while line:
        # print(line)
        list_file.append(line.strip('\n'))
        line = f.readline()

    instances = RobotGossipInfo.objects.all()
    instances.delete()

    str_question = ''
    str_answer = ''
    for i in list_file:
        if i == 'M':
            continue
        elif i.find("Q") != -1:
            str_question = i.strip('Q ')
        elif i.find("A") != -1:
            str_answer = i.strip('A ')
            if RobotGossipInfo.objects.filter(question=str_question).exists() == False:
                RobotGossipInfo.objects.create(question=str_question, answer=str_answer)
    print('Done')


def robot_basic_create_tags_withWeight(sentence):
    tags = jieba.analyse.extract_tags(sentence, topK=10, withWeight=True)
    return dict(tags)


def robot_basic_create_tags(sentence):
    tags = jieba.analyse.extract_tags(sentence, topK=10, withWeight=False)
    return tags


def robot_basic_similarity(array_input, dict_questions):
    len_input_tags = len(array_input)
    sim_sum = 0
    for i in range(len_input_tags):
       if array_input[i] in dict_questions:
           sim_sum += dict_questions[array_input[i]]
    return sim_sum


def robot_basic_weight_list(customer_input):
    instance_robotinfo = RobotGossipInfo.objects.all()
    if instance_robotinfo.exists() == False:
        return 0
    array_input_tags = robot_basic_create_tags(customer_input)
    weight_list = list()
    for i in instance_robotinfo:
        dict_questions_tags = robot_basic_create_tags_withWeight(i.question)
        weight = robot_basic_similarity(array_input_tags, dict_questions_tags) * i.weight
        weight_list.append([weight, i.answer])
    return weight_list
