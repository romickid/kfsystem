from .models import Customer, CommunicationKey
from django.core.mail import send_mail
import hashlib, random, string


def json_testing(json_receive, array_str, json_length):
    json = json_receive
    try:
        for i in array_str:
            json[i] = json[i]
    except KeyError:
        return 1
    if len(json) != json_length:
        return 2
    return 0


# useful
def customer_is_existent_by_email(email):
    try:
        instance = Customer.objects.get(email=email)
        return True
    except Customer.DoesNotExist:
        return False


# useful
def customer_is_existent_by_nickname(nickname):
    try:
        instance = Customer.objects.get(nickname=nickname)
        return True
    except Customer.DoesNotExist:
        return False


# useful
def customer_is_valid_by_email_password(email, sha512_final_password):
    try:
        instance = Customer.objects.get(email=email, password=sha512_final_password)
        return True
    except Customer.DoesNotExist:
        return False


# useful
def customer_generate_password(email, sha512_frontend_password):
    hash_email = hashlib.sha512()
    hash_email.update(email.encode('utf-8'))
    sha512_email = hash_email.hexdigest()
    hash_password = hashlib.sha512()
    hash_password.update((sha512_frontend_password+sha512_email+'customerbig5').encode('utf-8'))
    return hash_password.hexdigest()


# useful
def customer_sessions_check(request):
    try:
        request.session['ec_email'] = request.session['ec_email']
        return True
    except KeyError:
        return False


# useful
def customer_sessions_del(request):
    try:
        del request.session['ec_email']
    except KeyError:
        pass


# useful
def customer_generate_sending_data(request):
    email, nickname, telephone, location, description = '', '', '', '', ''
    if customer_sessions_check(request) == False:
        email = "匿名用户" + str((random.random() * 1000))
        nickname = "匿名用户"
        telephone = "empty"
        location = "empty"
        description = "empty"
    else:
        email = request.session['ec_email']
        instance = Customer.objects.get(email=email)
        nickname = instance.nickname
        telephone = instance.telephone
        location = instance.location
        description = instance.description
    return email, nickname, telephone, location, description


# useful
def communication_key_is_existent_by_myid(myid):
    try:
        instance = CommunicationKey.objects.get(myid=myid)
        return True
    except CommunicationKey.DoesNotExist:
        return False
