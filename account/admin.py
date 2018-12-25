from django.contrib import admin

# Register your models here.
from account.models import user
admin.site.register(user)