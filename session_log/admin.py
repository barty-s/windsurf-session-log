from django.contrib import admin
from .models import Session
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    """
    Class to customize Django admin display
    """
    list_display = ('author', 'title', 'date')
    list_filter = ('author', 'date')


# The following lines are added to remove the default django admin apps
admin.site.unregister(Site)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)
