from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Admin, CustomerService, ChattingLog, SerialNumber
from .serializers import AdminSerializer, CustomerServiceSerializer, ChattingLogSerializer, SerialNumberSerializer
from datetime import datetime, timedelta


@csrf_exempt
def admin_create(request):
    if request.method == 'POST':
        json_receive = JSONParser().parse(request)
        try:
            instance = Admin.objects.get(email=json_receive['email'])
            return HttpResponse('ERROR, email has been used.', status=400)
        except Admin.DoesNotExist:
            serializer = AdminSerializer(data=json_receive)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=403) # 401 just for test
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def admin_set_profile(request):
    if request.method == 'POST':
        json_receive = JSONParser().parse(request)
        try:
            json_receive['password'] = json_receive['password']
            json_receive['nickname'] = json_receive['nickname']
            instance = Admin.objects.get(email=json_receive['email'])
            serializer = AdminSerializer(instance, data=json_receive)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=401) # 401 just for test
            return JsonResponse(serializer.errors, status=400)
        except Admin.DoesNotExist:
            return HttpResponse('ERROR, email address is not exists.', status=400)
        except KeyError:
            return HttpResponse('ERROR, incomplete information.', status=400)


@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        json_receive = JSONParser().parse(request)
        serializer = AdminSerializer(data=json_receive)

        # TODO add SHA512 fuction

        try:
            instance = Admin.objects.get(email=json_receive['email'], password=json_receive['password'])
            return HttpResponse("Valid", status=401)  # 401 just for test
        except Admin.DoesNotExist:
            return HttpResponse("Invalid", status=400)


@csrf_exempt
def admin_reset_password(request):
    if request.method == 'POST':
        json_receive = JSONParser().parse(request)
        serializer = AdminSerializer(data=json_receive)

        # TODO add SHA512 fuction

        try:
            instance = Admin.objects.get(email=json_receive['email'], password=json_receive['password'])
            json_receive['password'] = json_receive['newpassword']
            serializer = AdminSerializer(instance, data=json_receive)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=401) # 401 just for test
            return HttpResponse("Completed", status=400)
        except Admin.DoesNotExist:
            return HttpResponse("Wrong Password or Email", status=400)


@csrf_exempt
def customerservice_create(request):
    if request.method == 'POST':
        json_receive = JSONParser().parse(request)
        try:
            instance = CustomerService.objects.get(email=json_receive['email'])
            return HttpResponse('ERROR, email has been used.', status=400)
        except CustomerService.DoesNotExist:
            serializer = CustomerServiceSerializer(data=json_receive)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=401) # 401 just for test
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def customerservice_set_profile(request):
    if request.method == 'POST':
        json_receive = JSONParser().parse(request)
        try:
            json_receive['password'] = json_receive['password']
            json_receive['nickname'] = json_receive['nickname']
            instance = CustomerService.objects.get(email=json_receive['email'])
            serializer = CustomerServiceSerializer(instance, data=json_receive)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=401) # 401 just for test
            return JsonResponse(serializer.errors, status=400)
        except CustomerService.DoesNotExist:
            return HttpResponse(status=404)
        except KeyError:
            return HttpResponse('ERROR, incomplete information.', status=400)


@csrf_exempt
def customerservice_login(request):
    if request.method == 'POST':
        json_receive = JSONParser().parse(request)
        serializer = CustomerServiceSerializer(data=json_receive)

        # TODO add SHA512 fuction

        try:
            instance = CustomerService.objects.get(email=json_receive['email'], password=json_receive['password'])
            return HttpResponse("Valid", status=401)  # 401 just for test
        except CustomerService.DoesNotExist:
            return HttpResponse("Invalid", status=400)


@csrf_exempt
def customerservice_reset_password(request):
    if request.method == 'POST':
        json_receive = JSONParser().parse(request)
        serializer = CustomerServiceSerializer(data=json_receive)

        # TODO add SHA512 fuction

        try:
            instance = CustomerService.objects.get(email=json_receive['email'], password=json_receive['password'])
            json_receive['password'] = json_receive['newpassword']
            serializer = CustomerServiceSerializer(instance, data=json_receive)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=401) # 401 just for test
            return HttpResponse("Completed", status=400)
        except CustomerService.DoesNotExist:
           return HttpResponse("Wrong Password or Email", status=400)


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


@csrf_exempt
def serialnumber_validity(request):
    if request.method == 'POST':
        json_receive = JSONParser().parse(request)
        serializer = SerialNumberSerializer(data=json_receive)
        try:
            instance = SerialNumber.objects.get(serials=json_receive['serials'])
            if instance.is_used == True:
                return HttpResponse("Invalid, the number has been used", status=400)
            else:
                return HttpResponse("Valid", status=401)  # 401 just for test
        except SerialNumber.DoesNotExist:
            return HttpResponse("Invalid, the number is not exist", status=400)


@csrf_exempt
def serialnumber_mark_used(request):
    if request.method == 'POST':
        json_receive = JSONParser().parse(request)
        try:
            instance = SerialNumber.objects.get(serials=json_receive['serials'])
            if instance.is_used == True:
                return HttpResponse("ERROR, serials number was used", status=400)
            json_receive['is_used'] = True
            serializer = SerialNumberSerializer(instance, data=json_receive)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse("Serials number is used", status=401)  # 401 just for test
            return JsonResponse('Invalid', status=400)
        except SerialNumber.DoesNotExist:
            return HttpResponse("Invalid, number is wrong", status=400)
