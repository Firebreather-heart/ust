from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = ['email','date_of_birth','about']

admin.site.register(get_user_model(),CustomUserAdmin)