from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Admin, CustomerService, ChattingLog, SerialNumber
from .serializers import AdminSerializer, CustomerServiceSerializer, ChattingLogSerializer, SerialNumberSerializer
from datetime import datetime, timedelta
import hashlib


@csrf_exempt
def admin_create(request):
    if request.method == 'POST':
        # Admin: email nickname password  SerialNumber: serials
        json_receive = JSONParser().parse(request)
        try:
            json_receive['email'] = json_receive['email']
            json_receive['nickname'] = json_receive['nickname']
            json_receive['password'] = json_receive['password']
            json_receive['serials'] = json_receive['serials']
        except KeyError:
            return HttpResponse('ERROR, incomplete information.', status=400)
        if sn_is_serials_valid(json_receive['serials']) == False:
            return HttpResponse('ERROR, serials is invalid.', status=400)
        if admin_is_existent_by_email(json_receive['email']) == True:
            return HttpResponse('ERROR, email has been registered.', status=400)
        if len(json_receive) != 4:
            return HttpResponse('ERROR, wrong information.', status=400)

        json_receive['password'] = admin_generate_password(json_receive['email'], json_receive['password'])
        json_receive['web_url'] = json_receive['email'] + '.web_url' # TODO change to a fancy url
        json_receive['widget_url'] = json_receive['email'] + '.widget_url'
        json_receive['mobile_url'] = json_receive['email'] + '.mobile_url'
        json_receive['communication_key'] = json_receive['email'] + '.communication_key' # TODO MD5 + salt
        serializer = AdminSerializer(data=json_receive)
        if serializer.is_valid():
            serializer.save()
            sn_mark_used(json_receive['serials'])
            return JsonResponse(serializer.data, status=401) # 401 For Test
        return HttpResponse('ERROR, invalid data in serializer.', status=400)


@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        # Admin: email password
        json_receive = JSONParser().parse(request)
        try:
            json_receive['email'] = json_receive['email']
            json_receive['password'] = json_receive['password']
        except KeyError:
            return HttpResponse('ERROR, incomplete information.', status=400)
        if len(json_receive) != 2:
            return HttpResponse('ERROR, wrong information.', status=400)

        sha512_final_password = admin_generate_password(json_receive['email'], json_receive['password'])
        if admin_is_valid_by_email_password(json_receive['email'], sha512_final_password) == True:
            return HttpResponse("Valid.", status=401)  # 401 just for test
        else:
            return HttpResponse("ERROR, wrong email or password.", status=400)


@csrf_exempt
def admin_reset_password(request):
    if request.method == 'POST':
        # Admin: email password newpassword
        json_receive = JSONParser().parse(request)
        try:
            json_receive['email'] = json_receive['email']
            json_receive['password'] = json_receive['password']
            json_receive['newpassword'] = json_receive['newpassword']
        except KeyError:
            return HttpResponse('ERROR, incomplete information.', status=400)
        if len(json_receive) != 3:
            return HttpResponse('ERROR, wrong information.', status=400)

        sha512_old_final_password = admin_generate_password(json_receive['email'], json_receive['password'])
        if admin_is_valid_by_email_password(json_receive['email'], sha512_old_final_password) == False:
            return HttpResponse("ERROR, wrong email or password.", status=400)

        sha512_new_final_password = admin_generate_password(json_receive['email'], json_receive['newpassword'])
        instance = Admin.objects.get(email=json_receive['email'], password=sha512_old_final_password)
        json_receive['password'] = sha512_new_final_password
        serializer = AdminSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=401) # 401 just for test
        else:
            return HttpResponse("ERROR, invalid data in serializer.", status=400)


@csrf_exempt
def customerservice_create(request):
    if request.method == 'POST':
        # CustomerService: email
        json_receive = JSONParser().parse(request)
        try:
            json_receive['email'] = json_receive['email']
        except KeyError:
            return HttpResponse('ERROR, incomplete information.', status=400)
        if cs_is_existent_by_email(json_receive['email']) == True:
            return HttpResponse('ERROR, email has been registered.', status=400)
        if len(json_receive) != 1:
            return HttpResponse('ERROR, wrong information.', status=400)

        serializer = CustomerServiceSerializer(data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=401) # 401 just for test
        return HttpResponse('ERROR, invalid data in serializer.', status=400)


@csrf_exempt
def customerservice_set_profile(request):
    if request.method == 'POST':
        # CustomerService: email password nickname
        json_receive = JSONParser().parse(request)
        try:
            json_receive['emil'] = json_receive['email']
            json_receive['password'] = json_receive['password']
            json_receive['nickname'] = json_receive['nickname']
        except KeyError:
            return HttpResponse('ERROR, incomplete information.', status=400)
        if cs_is_existent_by_email(json_receive['email']) == False:
            return HttpResponse('ERROR, email has not been registered.', status=400)
        if len(json_receive) != 3:
            return HttpResponse('ERROR, wrong information.', status=400)

        instance = CustomerService.objects.get(email=json_receive['email'])
        serializer = CustomerServiceSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=401) # 401 just for test
        return HttpResponse('ERROR, invalid data in serializer.', status=400)


@csrf_exempt
def customerservice_login(request):
    if request.method == 'POST':
        # CustomerService: email password
        json_receive = JSONParser().parse(request)
        try:
            json_receive['email'] = json_receive['email']
            json_receive['password'] = json_receive['password']
        except KeyError:
            return HttpResponse('ERROR, incomplete information.', status=400)
        if len(json_receive) != 2:
            return HttpResponse('ERROR, wrong information.', status=400)

        # TODO add SHA512 fuction

        if cs_is_valid_by_email_password(json_receive['email'], json_receive['password']) == True:
            return HttpResponse("Valid.", status=401)  # 401 just for test
        else:
            return HttpResponse("ERROR, wrong email or password.", status=400)


@csrf_exempt
def customerservice_reset_password(request):
    if request.method == 'POST':
        # CustomerService: email password newpassword
        json_receive = JSONParser().parse(request)
        try:
            json_receive['email'] = json_receive['email']
            json_receive['password'] = json_receive['password']
            json_receive['newpassword'] = json_receive['newpassword']
        except KeyError:
            return HttpResponse('ERROR, incomplete information.', status=400)
        if len(json_receive) != 3:
            return HttpResponse('ERROR, wrong information.', status=400)
        if cs_is_valid_by_email_password(json_receive['email'], json_receive['password']) == False:
            return HttpResponse("ERROR, wrong email or password.", status=400)

        # TODO add SHA512 fuction

        instance = CustomerService.objects.get(email=json_receive['email'], password=json_receive['password'])
        json_receive['password'] = json_receive['newpassword']
        serializer = CustomerServiceSerializer(instance, data=json_receive)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=401) # 401 just for test
        else:
            return HttpResponse("ERROR, invalid data in serializer.", status=400)


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
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def chattinglog_delete_record(request):
    if request.method == 'DELETE':
        chattinglogs = ChattingLog.objects.all()
        chattinglogs.delete()
        return HttpResponse(status=204)


@csrf_exempt
def chattinglog_delete_record_ontime(request):
    if request.method == 'DELETE':
        now = datetime.now()
        end_date = datetime(now.year, now.month, now.day, 0, 0) 
        start_date = end_date - timedelta(days=100)
        chattinglogs = ChattingLog.objects.filter(time__range=[start_date, end_date])            
        chattinglogs.delete()
        return HttpResponse(status=204)


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
        return JsonResponse(serializer1.errors, status=400)


def admin_is_existent_by_email(email):
    try:
        instance = Admin.objects.get(email=email)
        return True
    except Admin.DoesNotExist:
        return False


def admin_is_valid_by_email_password(email, password):
    try:
        instance = Admin.objects.get(email=email, password=password)
        return True
    except Admin.DoesNotExist:
        return False


def admin_generate_password(email, sha512_frontend_password):
    hash_email = hashlib.sha512()
    hash_email.update(email.encode('utf-8'))
    sha512_email = hash_email.hexdigest()
    hash_password = hashlib.sha512()
    hash_password.update((sha512_frontend_password+sha512_email+'big5').encode('utf-8'))
    return hash_password.hexdigest()


def sn_is_serials_valid(serials):
    try:
        instance = SerialNumber.objects.get(serials=serials)
        if instance.is_used == True:
            return False
        else:
            return True
    except SerialNumber.DoesNotExist:
        return False


def sn_mark_used(serials):
    if sn_is_serials_valid(serials) == False:
        return False
    else:
        instance = SerialNumber.objects.get(serials=serials)
        instance.is_used = True
        instance.save()
        return True


def cs_is_existent_by_email(email):
    try:
        instance = CustomerService.objects.get(email=email)
        return True
    except CustomerService.DoesNotExist:
        return False


def cs_is_valid_by_email_password(email, password):
    try:
        instance = CustomerService.objects.get(email=email, password=password)
        return True
    except CustomerService.DoesNotExist:
        return False
