from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Admin
from .serializers import AdminSerializer
from .views_helper_functions import *
from .views_check_functions import *
import hashlib
import random

@csrf_exempt
def admin_create(request):
    if request.method == 'POST':
        # Admin: email nickname password 
        json_receive = JSONParser().parse(request)
        is_correct, error_message = admin_create_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)
        json_receive['password'] = admin_generate_password(json_receive['email'], json_receive['password'])
        # json_receive['communication_key'] = admin_generate_communication_key(json_receive['email'])
        serializer = AdminSerializer(data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
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
            # cs_sessions_del(request)
            request.session['a_email'] = json_receive['email']
            return HttpResponse(request.session['a_email'], status=200)
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
            return JsonResponse(serializer.data, status=200)
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
        # json_receive['vid'] = admin_generate_vid(json_receive['email'])
        serializer = AdminSerializer(instance, data=json_receive)
        content = '尊敬的' + instance.nickname + ':\n' + '您提交了找回密码的请求，请点击如下链接，对密码进行修改。\n' + 'http://192.168.55.33:8000/admin_forget_password_page/?email=' + json_receive['email'] + '&key=' + json_receive['vid']
        if serializer.is_valid():
            serializer.save()
            admin_send_email_forget_password(json_receive['email'], content)
            return HttpResponse('Valid', status=200)
        else:
            return HttpResponse("ERROR, invalid data in serializer.", status=200)


@csrf_exempt
def admin_forget_password_save_data(request):
    if request.method == 'POST':
        # Admin: email newpassword
        json_receive = JSONParser().parse(request)
        is_correct, error_message = admin_forget_password_save_data_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        instance = Admin.objects.get(email=json_receive['email'])
        sha512_new_final_password = admin_generate_password(json_receive['email'], json_receive['newpassword'])
        json_receive['password'] = sha512_new_final_password
        serializer = AdminSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
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
def admin_send_info(request):
    if request.method == 'POST':
        # no json
        data_email = request.session['a_email']
        instance = Admin.objects.get(email=data_email)
        hash_key = hashlib.md5()
        hash_key.update((instance.email+instance.nickname).encode('utf-8'))
        data = 'http://192.168.55.33:8000/customer_newlabel/customer_newlabel.html?email=' + instance.email + '&nickname=' + instance.nickname + '&information=' + instance.info + '&' + hash_key.hexdigest()
        return HttpResponse(data, status=200) 


@csrf_exempt
def admin_send_info_v(request):
    if request.method == 'POST':
        # no json
        hash_key = hashlib.md5()
        hash_key.update((instance.email+instance.nickname).encode('utf-8'))
        data = 'http://192.168.55.33:8000/customer_newlabel/customer_newlabel.html?email=' + '-1' + '&nickname=' + 'none' + '&information=' + 'none' + '&' + hash_key.hexdigest()
        return HttpResponse(data, status=200) 


@csrf_exempt
def admin_logout(request):
    if request.method == 'POST':
        # no json
        is_correct, error_message = admin_logout_check(request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        del request.session['a_email']
        return HttpResponse('Logout ok.', status=200)


@csrf_exempt
def admin_get_info(request):
    if request.method == 'POST':
        # no json
        is_correct = admin_sessions_check(request)
        if is_correct == False:
            email = str((random.random() * 1000))
            hash_key = hashlib.sha512()
            hash_key.update((email).encode('utf-8'))
            data = 'http://192.168.55.33:8000/customer_newlabel/customer_newlabel.html?email=' + email + '&nickname=visitor' + '&information=' + 'No informations' + '&signature=' + hash_key.hexdigest()
            return HttpResponse(data, status=200)
        data_email = request.session['a_email']
        instance = Admin.objects.get(email=data_email)
        hash_key = hashlib.sha512()
        hash_key.update((instance.email+instance.nickname).encode('utf-8'))
        data = 'http://192.168.55.33:8000/customer_newlabel/customer_newlabel.html?email=' + instance.email + '&nickname=' + instance.nickname + '&information=' + instance.info + '&signature=' + hash_key.hexdigest()
        return HttpResponse(data, status=200)



@csrf_exempt
def admin_get_info_iframe(request):
    if request.method == 'POST':
        # no json
        is_correct = admin_sessions_check(request)
        if is_correct == False:
            email = str((random.random() * 1000))
            hash_key = hashlib.sha512()
            hash_key.update((email).encode('utf-8'))
            data = 'http://192.168.55.33:8000/customer_iframe/customer_iframe.html?email=' + email + '&nickname=visitor' + '&information=' + 'No informations' + '&signature=' + hash_key.hexdigest()
            # data = 'http://192.168.55.33:8000/customer_iframe/customer_iframe.html'
            return HttpResponse(data, status=200)
        data_email = request.session['a_email']
        instance = Admin.objects.get(email=data_email)
        hash_key = hashlib.sha512()
        hash_key.update((instance.email+instance.nickname).encode('utf-8'))
        data = 'http://192.168.55.33:8000/customer_iframe/customer_iframe.html?email=' + instance.email + '&nickname=' + instance.nickname + '&information=' + instance.info + '&signature=' + hash_key.hexdigest()
        # data = 'http://192.168.55.33:8000/customer_iframe/customer_iframe.html'
        return HttpResponse(data, status=200)