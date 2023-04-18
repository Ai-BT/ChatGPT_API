from django.contrib import admin

from .models import Users

# paiadmin
# 1234

class UserList(admin.ModelAdmin):
    list_display = ('userName', 'userPhone')


# Register your models here.
admin.site.register(Users, UserList)
