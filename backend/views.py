from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Admin, CustomerService, ChattingLog
from .serializers import AdminSerializer, CustomerServiceSerializer, ChattingLogSerializer

@csrf_exempt
def admin_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdminSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=401) # 401 just for test
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def admin_set_profile(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            snippet = Admin.objects.get(email = data['email'])
            serializer1 = AdminSerializer(snippet, data = data)
            if serializer1.is_valid():
                serializer1.save()
                return JsonResponse(serializer1.data, status = 401) # 401 just for test
            return JsonResponse(serializer1.errors, status = 400)
        except Admin.DoesNotExist:
            return HttpResponse(status=404)


@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdminSerializer(data=data)

        # TODO add SHA512 fuction

        try:
            snippet = Admin.objects.get(email = data['email'], password = data['password'])
            return HttpResponse("Valid", status = 401)  # 401 just for test
        except Admin.DoesNotExist:
            return HttpResponse("Invalid", status = 400)


@csrf_exempt
def admin_reset_password(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdminSerializer(data=data)

        # TODO add SHA512 fuction

        try:
            snippet = Admin.objects.get(email = data['email'], password = data['password'])
            data['password'] = data['newpassword']
            serializer = AdminSerializer(snippet, data = data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status = 401) # 401 just for test
            return HttpResponse("Completed", status = 400)
        except Admin.DoesNotExist:
            return HttpResponse("Wrong Password or Email", status = 400)

@csrf_exempt
def customerservice_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerServiceSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=401) # 401 just for test
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def customerservice_set_profile(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            snippet = CustomerService.objects.get(email = data['email'])
            serializer1 = CustomerServiceSerializer(snippet, data = data)
            if serializer1.is_valid():
                serializer1.save()
                return JsonResponse(serializer1.data, status = 401) # 401 just for test
            return JsonResponse(serializer1.errors, status = 400)
        except CustomerService.DoesNotExist:
            return HttpResponse(status=404)


@csrf_exempt
def customerservice_login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerServiceSerializer(data=data)

        # TODO add SHA512 fuction

        try:
            snippet = CustomerService.objects.get(email = data['email'], password = data['password'])
            return HttpResponse("Valid", status = 401)  # 401 just for test
        except CustomerService.DoesNotExist:
            return HttpResponse("Invalid", status = 400)


@csrf_exempt
def customerservice_reset_password(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerServiceSerializer(data=data)

        # TODO add SHA512 fuction

        try:
            snippet = CustomerService.objects.get(email = data['email'], password = data['password'])
            data['password'] = data['newpassword']
            serializer = CustomerServiceSerializer(snippet, data = data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status = 401) # 401 just for test
            return HttpResponse("Completed", status = 400)
        except CustomerService.DoesNotExist:
            return HttpResponse("Wrong Password or Email", status = 400)


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




 