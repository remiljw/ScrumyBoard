from django.contrib import admin
from remiljscrumy.models import *
from django.contrib.auth.models import User
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(GoalStatus)
admin.site.register(ScrumyHistory)
admin.site.register(ScrumyGoals)
admin.site.register(ScrumUser)
admin.site.register(ScrumProjectRole)
admin.site.register(ScrumProject)




# UserAdmin.fieldsets += ('Custom fields set', {'fields': ('role',)}),

# class CustomUserAdmin(UserAdmin):
# 	add_form = CustomUserCreationForm
# 	form = CustomUserChangeForm
# 	model = CustomUser
# 	list_display = ['email', 'username', 'role', 'pwd_reset_token','subscription']

admin.site.register(CustomUser,)

admin.site.register(Unsubscriber)
