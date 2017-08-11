from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Admin, CustomerService, ChattingLog, SerialNumber, EnterpriseDisplayInfo
from .serializers import AdminSerializer, CustomerServiceSerializer, CustomerServiceCreateSerializer, ChattingLogSerializer, SerialNumberSerializer, EnterpriseDisplayInfoSerializer
from datetime import datetime, timedelta
from .views_helper_functions import *
from .views_check_functions import *


@csrf_exempt
def admin_create(request):
    if request.method == 'POST':
        # Admin: email nickname password  SerialNumber: serials
        json_receive = JSONParser().parse(request)
        is_correct, error_message = admin_create_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)
        json_receive['password'] = admin_generate_password(json_receive['email'], json_receive['password'])
        json_receive['web_url'] = json_receive['email'] + '.web_url' # TODO change to a fancy url
        json_receive['widget_url'] = json_receive['email'] + '.widget_url'
        json_receive['mobile_url'] = json_receive['email'] + '.mobile_url'
        json_receive['communication_key'] = admin_generate_communication_key(json_receive['email'])
        json_receive['vid'] = admin_generate_vid(json_receive['email'])
        serializer = AdminSerializer(data=json_receive)
        if serializer.is_valid():
            serializer.save()
            sn_mark_used(json_receive['serials'])
            return HttpResponse('OK', status=200)
        return HttpResponse('ERROR, invalid data in serializer.', status=200)


@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        # Admin: email password
        json_receive = JSONParser().parse(request)
        is_correct, error_message = admin_login_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)
        sha512_final_password = admin_generate_password(json_receive['email'], json_receive['password'])
        if admin_is_valid_by_email_password(json_receive['email'], sha512_final_password) == True:
            cs_sessions_del(request)
            request.session['a_email'] = json_receive['email']
            return HttpResponse('OK', status=200)
        else:
            return HttpResponse("ERROR, wrong email or password.", status=200)


@csrf_exempt
def admin_reset_password(request):
    if request.method == 'POST':
        # Admin: password newpassword
        json_receive = JSONParser().parse(request)
        is_correct, error_message = admin_reset_password_check(json_receive, request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)
        
        json_receive['email'] = request.session['a_email']
        sha512_old_final_password = admin_generate_password(json_receive['email'], json_receive['password'])
        if admin_is_valid_by_email_password(json_receive['email'], sha512_old_final_password) == False:
            return HttpResponse("ERROR, wrong email or password.", status=200)
        sha512_new_final_password = admin_generate_password(json_receive['email'], json_receive['newpassword'])
        instance = Admin.objects.get(email=json_receive['email'], password=sha512_old_final_password)
        json_receive['password'] = sha512_new_final_password
        serializer = AdminSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('OK', status=200)
        return HttpResponse("ERROR, invalid data in serializer.", status=200)


@csrf_exempt
def admin_forget_password_email_request(request):
    if request.method == 'POST':
        # Admin: email
        json_receive = JSONParser().parse(request)
        is_correct, error_message = admin_forget_password_email_request_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        instance = Admin.objects.get(email=json_receive['email'])
        json_receive['vid'] = admin_generate_vid(json_receive['email'])
        serializer = AdminSerializer(instance, data=json_receive)
        content = '尊敬的' + instance.nickname + ':\n' + '您提交了找回密码的请求，请点击如下链接，对密码进行修改。\n' + 'http://192.168.55.33:8000/admin_forget_password_page/?email=' + json_receive['email'] + '&key=' + json_receive['vid']
        if serializer.is_valid():
            serializer.save()
            admin_send_email_forget_password(json_receive['email'], content)
            return HttpResponse('OK', status=200)
        return HttpResponse("ERROR, invalid data in serializer.", status=200)


@csrf_exempt
def admin_forget_password_check_vid(request):
    if request.method == 'POST':
        # Admin: email vid
        json_receive = JSONParser().parse(request)
        is_correct, error_message = admin_forget_password_check_vid_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        json_receive['vid'] = admin_generate_vid(json_receive['email'])
        instance = Admin.objects.get(email=json_receive['email'])
        serializer = AdminSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json_receive['vid'], status=200)
        return HttpResponse("ERROR, invalid data in serializer.", status=200)


@csrf_exempt
def admin_forget_password_save_data(request):
    if request.method == 'POST':
        # Admin: email newpassword vid
        json_receive = JSONParser().parse(request)
        is_correct, error_message = admin_forget_password_save_data_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        instance = Admin.objects.get(email=json_receive['email'])
        sha512_new_final_password = admin_generate_password(json_receive['email'], json_receive['newpassword'])
        json_receive['password'] = sha512_new_final_password
        json_receive['vid'] = admin_generate_vid(json_receive['email'])
        serializer = AdminSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('OK', status=200)
        return HttpResponse("ERROR, invalid data in serializer.", status=200)


@csrf_exempt
def admin_show_communication_key(request):
    if request.method == 'POST':
        # no json
        is_correct, error_message = admin_show_communication_key_check(request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        data_email = request.session['a_email']
        communication_key = admin_get_communication_key(data_email)
        json_send = {'communication_key': communication_key}
        return JsonResponse(json_send, status=200)


@csrf_exempt
def admin_reset_communication_key(request):
    if request.method == 'POST':
        # no json
        is_correct, error_message = admin_reset_communication_key_check(request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        json_receive = dict()
        json_receive['email'] = request.session['a_email']
        instance = Admin.objects.get(email=json_receive['email'])
        json_receive['communication_key'] = admin_generate_communication_key(json_receive['email'])
        serializer = AdminSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('OK', status=200)
        return HttpResponse('ERROR, invalid data in serializer.', status=200)


@csrf_exempt
def admin_show_cs_status(request):
    if request.method == 'POST':
        # no json
        is_correct, error_message = admin_show_cs_status_check(request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        data_email = request.session['a_email']
        instance_admin = Admin.objects.get(email=data_email)
        instance_customerservice = CustomerService.objects.filter(enterprise=instance_admin.id)
        json_send = list()
        for i in instance_customerservice:
            json_send.append({'email': i.email, 'is_register': i.is_register, 'is_online': i.is_online, 'connection_num': i.connection_num, 'nickname': i.nickname})
        return JsonResponse(json_send, safe=False, status=200)


@csrf_exempt
def admin_show_user_status(request):
    if request.method == 'POST':
        # no json
        is_correct, error_message = admin_show_user_status_check(request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        data_email = request.session['a_email']
        instance = Admin.objects.get(email=data_email)
        json_send = {'email': instance.email, 'nickname': instance.nickname}
        return JsonResponse(json_send, status=200)


@csrf_exempt
def admin_display_info_create(request):
    if request.method == 'POST':
        # EnterpriseInfoType: name comment
        json_receive = JSONParser().parse(request)
        is_correct, error_message = admin_display_info_create_check(json_receive, request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        data_email = request.session['a_email']
        instance_admin = Admin.objects.get(email=data_email)
        json_receive['enterprise'] = instance_admin.id
        serializer = EnterpriseDisplayInfoSerializer(data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('OK', status=200)
        return HttpResponse('ERROR, invalid data in serializer.', status=200)


@csrf_exempt
def admin_display_info_delete(request):
    if request.method == 'POST':
        # EnterpriseInfoType: name
        json_receive = JSONParser().parse(request)
        is_correct, error_message = admin_display_info_delete_check(json_receive, request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        data_email = request.session['a_email']
        instance_admin = Admin.objects.get(email=data_email)
        instance_displayinfo = EnterpriseDisplayInfo.objects.filter(enterprise=instance_admin.id, name=json_receive['name'])
        instance_displayinfo.delete()
        return HttpResponse('OK', status=200)


@csrf_exempt
def admin_display_info_show(request):
    if request.method == 'POST':
        # no json
        is_correct, error_message = admin_display_info_show_check(request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        admin_email = request.session['a_email']
        instance_admin = Admin.objects.get(email=admin_email)
        instance_displayinfo = EnterpriseDisplayInfo.objects.filter(enterprise=instance_admin.id)
        json_send = list()
        for i in instance_displayinfo:
            json_send.append({'name': i.name, 'comment': i.comment})
        return JsonResponse(json_send, safe=False, status=200)


@csrf_exempt
def admin_logout(request):
    if request.method == 'POST':
        # no json
        is_correct, error_message = admin_logout_check(request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        del request.session['a_email']
        return HttpResponse('OK', status=200)


@csrf_exempt
def customerservice_create(request):
    if request.method == 'POST':
        # CustomerService: email
        json_receive = JSONParser().parse(request)
        is_correct, error_message = customerservice_create_check(json_receive, request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        admin_email = request.session['a_email']
        instance_admin = Admin.objects.get(email=admin_email)
        json_receive['nickname'] = json_receive['email']
        json_receive['enterprise'] = instance_admin.id
        json_receive['vid'] = cs_generate_vid(json_receive['email'])
        serializer = CustomerServiceCreateSerializer(data=json_receive)
        content = '尊敬的客服您好' + ':\n' + '请点击以下链接完成账号创建的剩余工作。\n' + 'http://192.168.55.33:8000/customerservice_create_page/?mail=' + json_receive['email'] + '&key=' + json_receive['vid']
        if serializer.is_valid():
            serializer.save()
            cs_send_email_create_account(json_receive['email'], content)
            return HttpResponse('OK', status=200)
        return HttpResponse('ERROR, invalid data in serializer.', status=200)


@csrf_exempt
def customerservice_set_profile(request):
    if request.method == 'POST':
        # CustomerService: email password nickname vid
        json_receive = JSONParser().parse(request)
        is_correct, error_message = customerservice_set_profile_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        json_receive['password'] = cs_generate_password(json_receive['email'], json_receive['password'])
        json_receive['vid'] = cs_generate_vid(json_receive['email'])
        instance = CustomerService.objects.get(email=json_receive['email'])
        serializer = CustomerServiceSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('OK', status=200)
        return HttpResponse('ERROR, invalid data in serializer.', status=200)


@csrf_exempt
def customerservice_set_profile_check_vid(request):
    if request.method == 'POST':
        # CustomerService: email vid
        json_receive = JSONParser().parse(request)
        is_correct, error_message = customerservice_set_profile_check_vid_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        json_receive['vid'] = cs_generate_vid(json_receive['email'])
        instance = CustomerService.objects.get(email=json_receive['email'])
        serializer = CustomerServiceSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('OK', status=200)
        return HttpResponse('ERROR, invalid data in serializer.', status=200)


@csrf_exempt
def customerservice_login(request):
    if request.method == 'POST':
        # CustomerService: email password
        json_receive = JSONParser().parse(request)
        is_correct, error_message = customerservice_login_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        sha512_final_password = cs_generate_password(json_receive['email'], json_receive['password'])
        if cs_is_valid_by_email_password(json_receive['email'], sha512_final_password) == True:
            admin_sessions_del(request)
            request.session['c_email'] = json_receive['email']
            return HttpResponse('OK', status=200) 
        return HttpResponse("ERROR, wrong email or password.", status=200)


@csrf_exempt
def customerservice_reset_password(request):
    if request.method == 'POST':
        # CustomerService: password newpassword
        json_receive = JSONParser().parse(request)
        is_correct, error_message = customerservice_reset_password_check(json_receive, request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        json_receive['email'] = request.session['c_email']
        sha512_old_final_password = cs_generate_password(json_receive['email'], json_receive['password'])
        if cs_is_valid_by_email_password(json_receive['email'], sha512_old_final_password) == False:
            return HttpResponse("ERROR, wrong email or password.", status=200)
        sha512_new_final_password = cs_generate_password(json_receive['email'], json_receive['newpassword'])
        instance = CustomerService.objects.get(email=json_receive['email'], password=sha512_old_final_password)
        json_receive['password'] = sha512_new_final_password
        serializer = CustomerServiceSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('OK', status=200)
        return HttpResponse("ERROR, invalid data in serializer.", status=200)


@csrf_exempt
def customerservice_forget_password_email_request(request):
    if request.method == 'POST':
        # CustomerService: email
        json_receive = JSONParser().parse(request)
        is_correct, error_message = customerservice_forget_password_email_request_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        instance = CustomerService.objects.get(email=json_receive['email'])
        json_receive['vid'] = cs_generate_vid(json_receive['email'])
        serializer = CustomerServiceSerializer(instance, data=json_receive)
        content = '尊敬的' + instance.nickname + ':\n' + '您提交了找回密码的请求，请点击如下链接，对密码进行修改。\n' + 'http://192.168.55.33:8000/customerservice_forget_password_page/?email=' + json_receive['email'] + '&key=' + json_receive['vid']
        if serializer.is_valid():
            serializer.save()
            cs_send_email_forget_password(json_receive['email'], content)
            return HttpResponse('OK', status=200)
        return HttpResponse("ERROR, invalid data in serializer.", status=200)


@csrf_exempt
def customerservice_forget_password_check_vid(request):
    if request.method == 'POST':
        # CustomerService: email vid
        json_receive = JSONParser().parse(request)
        is_correct, error_message = customerservice_forget_password_check_vid_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        json_receive['vid'] = cs_generate_vid(json_receive['email'])
        instance = CustomerService.objects.get(email=json_receive['email'])
        serializer = CustomerServiceSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json_receive['vid'], status=200)
        return HttpResponse("ERROR, invalid data in serializer.", status=200)


@csrf_exempt
def customerservice_forget_password_save_data(request):
    if request.method == 'POST':
        # CustomerService: email newpassword vid
        json_receive = JSONParser().parse(request)
        is_correct, error_message = customerservice_forget_password_save_data_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        instance = CustomerService.objects.get(email=json_receive['email'])
        sha512_new_final_password = cs_generate_password(json_receive['email'], json_receive['newpassword'])
        json_receive['password'] = sha512_new_final_password
        json_receive['vid'] = cs_generate_vid(json_receive['email'])
        serializer = CustomerServiceSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('OK', status=200)
        return HttpResponse("ERROR, invalid data in serializer.", status=200)


@csrf_exempt
def customerservice_show_user_status(request):
    if request.method == 'POST':
        # no json
        is_correct, error_message = customerservice_show_user_status_check(request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        data_email = request.session['c_email']
        instance = CustomerService.objects.get(email=data_email)
        json_send = {'email': instance.email, 'nickname': instance.nickname}
        return JsonResponse(json_send, status=200)


@csrf_exempt
def customerservice_logout(request):
    if request.method == 'POST':
        # no json
        is_correct, error_message = customerservice_logout_check(request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        del request.session['c_email']
        return HttpResponse('OK', status=200)


@csrf_exempt
def chattinglog_get_data(request):
    if request.method == 'GET':
        chattinglogs = ChattingLog.objects.all()
        serializer = ChattingLogSerializer(chattinglogs, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def chattinglog_send_message(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChattingLogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=200)


@csrf_exempt
def chattinglog_delete_record(request):
    if request.method == 'DELETE':
        chattinglogs = ChattingLog.objects.all()
        chattinglogs.delete()
        return HttpResponse(status=200)


@csrf_exempt
def chattinglog_delete_record_ontime(request):
    if request.method == 'DELETE':
        now = datetime.now()
        end_date = datetime(now.year, now.month, now.day, 0, 0)
        start_date = end_date - timedelta(days=100)
        chattinglogs = ChattingLog.objects.filter(time__range=[start_date, end_date])
        chattinglogs.delete()
        return HttpResponse(status=200)


@csrf_exempt
def chattinglog_status_change(request):
    if request.method == 'GET':
        customerservice = CustomerService.objects.get(nickname='lala')
        if customerservice.is_online == True:
            serializer = CustomerServiceSerializer(customerservice, data={'is_online': False}, partial=True)
        if customerservice.is_online == False:
            serializer = CustomerServiceSerializer(customerservice, data={'is_online': True}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer1.errors, status=200)

@csrf_exempt
def chattinglog_show_history(request):
    if request.method == 'POST':
        # Chattinglog: client_id service_id
        json_receive = JSONParser().parse(request)
        instances = ChattingLog.objects.filter(client_id=json_receive['client_id'], service_id=json_receive['service_id']).order_by('time')
        serializer = ChattingLogSerializer(instances,many=True)
        return JsonResponse(serializer.data,safe=False,status=200)
