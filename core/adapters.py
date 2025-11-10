from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Automatically link or create a user by email when logging in with Google.
    """

    def pre_social_login(self, request, sociallogin):
        """
        This hook is called just after a successful authentication from the
        social provider, but before the login is actually processed.

        If a user with this email already exists, link the social account
        to that existing user.
        """
        user = sociallogin.user
        if not user.email:
            return  # no email, cannot link

        try:
            existing_user = User.objects.get(email=user.email)
            sociallogin.connect(request, existing_user)
        except User.DoesNotExist:
            # New user will be created automatically by allauth
            pass
