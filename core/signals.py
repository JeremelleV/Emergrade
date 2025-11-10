from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(user_signed_up)
def populate_profile_on_signup(request, user, **kwargs):
    sociallogin = kwargs.get("sociallogin")
    if sociallogin:
        extra_data = sociallogin.account.extra_data
        user.first_name = extra_data.get("given_name", "")
        user.last_name = extra_data.get("family_name", "")
        user.save()
