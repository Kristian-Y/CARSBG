from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

UserModel = get_user_model()


# Register your models here.

@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    list_display = ("id", "first_name", "last_name", "email",)
    list_filter = ("id", "first_name", "last_name", "email",)
