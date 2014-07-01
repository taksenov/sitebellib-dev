from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from elcatuserprofile.models import chb

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = chb

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]

admin.site.register(User, UserProfileAdmin)
