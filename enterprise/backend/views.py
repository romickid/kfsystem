from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Customer, CommunicationKey
from .serializers import CustomerSerializer
from .views_helper_functions import *
from .views_check_functions import *
import hashlib
import random


@csrf_exempt
def customer_create(request):
    if request.method == 'POST':
        # Customer: email nickname password telephone location description
        json_receive = JSONParser().parse(request)
        is_correct, error_message = customer_create_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)
        json_receive['password'] = customer_generate_password(json_receive['email'], json_receive['password'])
        serializer = CustomerSerializer(data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return HttpResponse('ERROR, invalid data in serializer.', status=200)


@csrf_exempt
def customer_login(request):
    if request.method == 'POST':
        # Customer: email password
        json_receive = JSONParser().parse(request)
        is_correct, error_message = customer_login_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)
        sha512_final_password = customer_generate_password(json_receive['email'], json_receive['password'])
        if customer_is_valid_by_email_password(json_receive['email'], sha512_final_password) == True:
            request.session['ec_email'] = json_receive['email']
            return HttpResponse(request.session['ec_email'], status=200)
        else:
            return HttpResponse("ERROR, wrong email or password.", status=200)


@csrf_exempt
def customer_show_user_info(request):
    if request.method == 'POST':
        # no json
        is_correct, error_message = customer_show_user_info_check(request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        data_email = request.session['ec_email']
        instance = Customer.objects.get(email=data_email)
        json_send = {'email': instance.email, 'nickname': instance.nickname, 'telephone': instance.telephone, 'location': instance.location, 'description': instance.description}
        return JsonResponse(json_send, status=200)


@csrf_exempt
def customer_show_user_login_status(request):
    if request.method == 'POST':
        # no json
        isLogin = customer_sessions_check(request)
        return HttpResponse(isLogin, status=200)


@csrf_exempt
def customer_logout(request):
    if request.method == 'POST':
        # no json
        is_correct, error_message = customer_logout_check(request)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        del request.session['ec_email']
        return HttpResponse('Logout ok.', status=200)


@csrf_exempt
def communication_key_update(request):
    if request.method == 'POST':
        # CommunicationKey: communication_key
        json_receive = JSONParser().parse(request)
        is_correct, error_message = communication_key_update_check(json_receive)
        if is_correct == 0:
            return HttpResponse(error_message, status=200)

        if communication_key_is_existent_by_myid(1) == True:
            instance = CommunicationKey.objects.get(myid=1)
            instance.key = json_receive['communication_key']
            instance.save()
        else:
            CommunicationKey.objects.create(id=1, key=json_receive['communication_key'], myid=1)
        return HttpResponse('OK', status=200)


@csrf_exempt
def customer_get_web_url(request):
    if request.method == 'POST':
        # no json
        email, nickname, telephone, location, description = customer_generate_sending_data(request)
        if communication_key_is_existent_by_myid(1) == False:
            return HttpResponse('ERROR, communication key is not exist', status=200)
        communication_key = CommunicationKey.objects.get(myid = 1).key
        hash_key = hashlib.sha512()
        hash_key.update('demo'+email+nickname+communication_key).encode('utf-8')
        signature = hash_key.hexdigest()
        data = 'http://192.168.55.33:8000/web/demo/?email=' + email + '&nickname=' + nickname + '&telephone=' + telephone + '&location=' + location + '&description=' + description + '&signature=' + signature
        return HttpResponse(data, status=200)


@csrf_exempt
def customer_get_widget_url(request):
    if request.method == 'POST':
        # no json
        email, nickname, telephone, location, description = customer_generate_sending_data(request)
        if communication_key_is_existent_by_myid(1) == False:
            return HttpResponse('ERROR, communication key is not exist', status=200)
        communication_key = CommunicationKey.objects.get(myid = 1).key
        hash_key = hashlib.sha512()
        hash_key.update('demo'+email+nickname+communication_key).encode('utf-8')
        signature = hash_key.hexdigest()
        data = 'http://192.168.55.33:8000/widget/demo/?email=' + email + '&nickname='+ nickname + '&telephone=' + telephone + '&location=' + location + '&description=' + description + '&signature=' + signature
        return HttpResponse(data, status=200)


@csrf_exempt
def customer_get_mobile_url(request):
    if request.method == 'POST':
        # no json
        email, nickname, telephone, location, description = customer_generate_sending_data(request)
        if communication_key_is_existent_by_myid(1) == False:
            return HttpResponse('ERROR, communication key is not exist', status=200)
        communication_key = CommunicationKey.objects.get(myid = 1).key
        hash_key = hashlib.sha512()
        hash_key.update('demo'+email+nickname+communication_key).encode('utf-8')
        signature = hash_key.hexdigest()
        data = 'http://192.168.55.33:8000/mobile/demo/?email=' + email + '&nickname=' + nickname + '&telephone=' + telephone + '&location=' + location + '&description=' + description + '&signature=' + signature
        return HttpResponse(data, status=200)
