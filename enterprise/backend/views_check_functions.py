from .views_helper_functions import *


def customer_create_check(json_receive):
    test_json = json_testing(json_receive, ['email', 'nickname', 'password', 'telephone', 'location'], 5)
    if test_json == 1:
        return 0, 'ERROR, incomplete information.'
    if test_json == 2:
        return 0, 'ERROR, wrong information.'
    if customer_is_existent_by_email(json_receive['email']) == True:
        return 0, 'ERROR, email has been registered.'
    if customer_is_existent_by_nickname(json_receive['nickname']) == True:
        return 0, 'ERROR, nickname has been used.'
    return 1, 'No ERROR.'


def customer_login_check(json_receive):
    test_json = json_testing(json_receive, ['email', 'password'], 2)
    if test_json == 1:
        return 0, 'ERROR, incomplete information.'
    if test_json == 2:
        return 0, 'ERROR, wrong information.'
    return 1, 'No ERROR.'


def customer_show_user_info_check(request):
    test_sessions = customer_sessions_check(request)
    if test_sessions == False:
        return 0, 'ERROR, session is broken.'
    if customer_is_existent_by_email(request.session['ec_email']) == False:
        return 0, 'ERROR, wrong email.'
    return 1, 'No ERROR.'


def customer_logout_check(request):
    test_sessions = customer_sessions_check(request)
    if test_sessions == False:
        return 0, 'ERROR, session is broken.'
    if customer_is_existent_by_email(request.session['ec_email']) == False:
        return 0, 'ERROR, wrong email.'
    return 1, 'No ERROR.'


def communication_key_update_check(json_receive):
    test_json = json_testing(json_receive, ['communication_key'], 1)
    if test_json == 1:
        return 0, 'ERROR, incomplete information.'
    if test_json == 2:
        return 0, 'ERROR, wrong information.'
    if len(communication_key) != 32:
        return 0, 'ERROR, communication key error.'
    return 1, 'No ERROR.'
