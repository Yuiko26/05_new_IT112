from django.apps import AppConfig
from django.contrib.admin import apps

class MessageboardConfig(AppConfig):
    name = 'messageboard'

class MessageboardAdminConfig(apps.AdminConfig):
    default_site = 'admin.Comment8orAdminSite'