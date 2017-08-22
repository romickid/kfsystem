from .models import Admin
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


def admin_is_existent_by_email(email):
    try:
        instance = Admin.objects.get(email=email)
        return True
    except Admin.DoesNotExist:
        return False


def admin_is_existent_by_nickname(nickname):
    try:
        instance = Admin.objects.get(nickname=nickname)
        return True
    except Admin.DoesNotExist:
        return False


def admin_is_valid_by_email_password(email, sha512_final_password):
    try:
        instance = Admin.objects.get(email=email, password=sha512_final_password)
        return True
    except Admin.DoesNotExist:
        return False


def admin_generate_password(email, sha512_frontend_password):
    hash_email = hashlib.sha512()
    hash_email.update(email.encode('utf-8'))
    sha512_email = hash_email.hexdigest()
    hash_password = hashlib.sha512()
    hash_password.update((sha512_frontend_password+sha512_email+'adminbig5').encode('utf-8'))
    return hash_password.hexdigest()


def admin_generate_communication_key(email):
    salt1 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    salt2 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    hash_key = hashlib.md5()
    hash_key.update((salt1+email+salt2).encode('utf-8'))
    return hash_key.hexdigest()


def admin_get_communication_key(email):
    try:
        instance = Admin.objects.get(email=email)
        return instance.communication_key
    except Admin.DoesNotExist:
        return False


def admin_generate_vid(email):
    return admin_generate_communication_key(email)


def admin_send_email_forget_password(email, content):
    send_mail('客服系统找回密码', content, 'big5_nankai@163.com', [email], fail_silently=True)


def admin_is_existent_by_email_vid(email, vid):
    try:
        instance = Admin.objects.get(email=email, vid=vid)
        return True
    except Admin.DoesNotExist:
        return False


def admin_sessions_check(request):
    try:
        request.session['a_email'] = request.session['a_email']
        return True
    except KeyError:
        return False


def admin_sessions_del(request):
    try:
        del request.session['a_email']
    except KeyError:
        pass

