from django.conf import settings
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
 
class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
 
    def populate_user(self, request, sociallogin, data):
      user = super(CustomSocialAccountAdapter, self).populate_user(request, sociallogin, data)
      url = sociallogin.account.extra_data.get('picture', {}).get('data', {}).get('url')
      if url: user.profile_image_url = url
      return user