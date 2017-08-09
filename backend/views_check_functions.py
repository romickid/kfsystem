from .views_helper_functions import *


def admin_create_check(json_receive):
    test_result = json_testing(json_receive, ['email', 'nickname', 'password', 'serials'], 4)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    if sn_is_serials_valid(json_receive['serials']) == False:
        return 0, 'ERROR, serials is invalid.'
    if admin_is_existent_by_email(json_receive['email']) == True:
        return 0, 'ERROR, email has been registered.'
    if admin_is_existent_by_nickname(json_receive['nickname']) == True:
        return 0, 'ERROR, nickname has been used.'
    return 1, 'No ERROR.'


def admin_login_check(json_receive):
    test_result = json_testing(json_receive, ['email', 'password'], 2)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    return 1, 'No ERROR.'


def admin_reset_password_check(json_receive):
    test_result = json_testing(json_receive, ['email', 'password', 'newpassword'], 3)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    return 1, 'No ERROR.'


def admin_forget_password_email_request_check(json_receive):
    test_result = json_testing(json_receive, ['email'], 1)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    if admin_is_existent_by_email(json_receive['email']) == False:
        return 0, 'ERROR, wrong email.'
    return 1, 'No ERROR.'


def admin_forget_password_check_vid_check(json_receive):
    test_result = json_testing(json_receive, ['email', 'vid'], 2)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    if admin_is_existent_by_email_vid(json_receive['email'], json_receive['vid']) == False:
        return 0, 'ERROR, wrong email or vid.'
    return 1, 'No ERROR.'


def admin_forget_password_save_data_check(json_receive):
    test_result = json_testing(json_receive, ['email', 'newpassword'], 2)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    if admin_is_existent_by_email(json_receive['email']) == False:
        return 0, 'ERROR, wrong email.'
    return 1, 'No ERROR.'


def admin_show_communication_key_check(json_receive):
    test_result = json_testing(json_receive, ['email'], 1)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    return 1, 'No ERROR.'


def admin_reset_communication_key_check(json_receive):
    test_result = json_testing(json_receive, ['email'], 1)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    if admin_is_existent_by_email(json_receive['email']) == False:
        return 0, 'ERROR, wrong email.'
    return 1, 'No ERROR.'


def customerservice_create_check(json_receive):
    test_result = json_testing(json_receive, ['email', 'admin_email'], 2)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    if cs_is_existent_by_email(json_receive['email']) == True:
        return 0, 'ERROR, email has been registered.'
    if admin_is_existent_by_email(json_receive['admin_email']) == False:
        return 0, 'ERROR, admin_email is wrong.'
    return 1, 'No ERROR.'


def customerservice_set_profile_check(json_receive):
    test_result = json_testing(json_receive, ['email', 'password', 'nickname'], 3)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    if cs_is_existent_by_email(json_receive['email']) == False:
        return 0, 'ERROR, email has not been registered.'
    if cs_is_existent_by_nickname(json_receive['nickname']) == True:
        return 0, 'ERROR, nickname has been used.'
    return 1, 'No ERROR.'


def customerservice_login_check(json_receive):
    test_result = json_testing(json_receive, ['email', 'password'], 2)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    return 1, 'No ERROR.'


def customerservice_reset_password_check(json_receive):
    test_result = json_testing(json_receive, ['email', 'password', 'newpassword'], 3)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    return 1, 'No ERROR.'


def customerservice_forget_password_email_request_check(json_receive):
    test_result = json_testing(json_receive, ['email'], 1)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    if cs_is_existent_by_email(json_receive['email']) == False:
        return 0, 'ERROR, wrong email.'
    return 1, 'No ERROR.'


def customerservice_forget_password_check_vid_check(json_receive):
    test_result = json_testing(json_receive, ['email', 'vid'], 2)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    if cs_is_existent_by_email_vid(json_receive['email'], json_receive['vid']) == False:
        return 0, 'ERROR, wrong email or vid.'
    return 1, 'No ERROR.'


def customerservice_forget_password_save_data_check(json_receive):
    test_result = json_testing(json_receive, ['email', 'newpassword'], 2)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    if cs_is_existent_by_email(json_receive['email']) == False:
        return 0, 'ERROR, wrong email.'
    return 1, 'No ERROR.'


def customerservice_show_status_check(json_receive):
    test_result = json_testing(json_receive, ['admin_email'], 1)
    if test_result == 1:
        return 0, 'ERROR, incomplete information.'
    if test_result == 2:
        return 0, 'ERROR, wrong information.'
    if admin_is_existent_by_email(json_receive['admin_email']) == False:
        return 0, 'ERROR, wrong admin_email.'
    return 1, 'No ERROR.'
