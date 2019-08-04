from django.contrib import admin
from .models import employees,user_auth
# Register your models here.
admin.site.register(employees)
admin.site.register(user_auth)
