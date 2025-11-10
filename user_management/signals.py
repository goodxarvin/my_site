from django.contrib.auth.signals import user_logged_in
from allauth.account.signals import user_signed_up
from django.dispatch import receiver


@receiver(user_logged_in)
def extended_session(sender, request, user, **kwargs):
    if request.POST.get("remember"):
        request.session.set_expiry(3600*24)  # one day
    else:
        request.session.set_expiry(0)


# @receiver(user_signed_up)
# def signed_up_user_receiver(request, user, **kwargs):
#     gender = request.POST.get('gender')
#     if gender:
#         user.gender = gender
#         gender.save()
