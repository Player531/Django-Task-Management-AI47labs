from django.contrib import admin
from .models import OAuthKeys, SendInvitation
from django.urls import path
from .views import invite_user

class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('invite/', self.admin_view(invite_user), name='invite_user')
        ]
        return custom_urls + urls

admin_site = CustomAdminSite(name='custom_admin')
admin_site.register(OAuthKeys)
admin_site.register(SendInvitation)
