from django.contrib import admin
from .models import User

class LoginProjModelAdmin(admin.ModelAdmin):
    list_display = ('username','email','firstname', 'lastname','password')

admin.site.register(User, LoginProjModelAdmin)