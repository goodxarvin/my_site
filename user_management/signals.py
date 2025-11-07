from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


@receiver(user_logged_in)
def extended_session(sender, request, user, **kwargs):
    if request.POST.get("remember"):
        request.session.set_expiry(3600*24)  # one day
    else:
        request.session.set_expiry(0)


# from django.contrib.auth.signals import user_logged_in
# from django.dispatch import receiver


# @receiver(user_logged_in)
# def extended_session(sender, request, user, **kwargs):
#     if request.POST.get('remember'):
#         # مدت session طولانی (مثلاً 30 روز)
#         request.session.set_expiry(60 * 60 * 24 * 30)  # 30 روز
#     else:
#         # session عادی (با بستن مرورگر تموم میشه)
#         request.session.set_expiry(0)
