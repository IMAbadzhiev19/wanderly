from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from wanderly.accounts.forms import AppUserCreationForm, AppUserChangeForm

UserModel = get_user_model()

@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    form = AppUserChangeForm
    add_form = AppUserCreationForm

    list_display = ('username', 'email')

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        ('Credentials', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',)})
    )


@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    staff_group, created = Group.objects.get_or_create(name='staff_group')
    superuser_group, created = Group.objects.get_or_create(name='superuser_group')

    staff_permissions = Permission.objects.filter(codename__in=['view_trip', 'add_trip', 'edit_trip', 'delete_trip'])
    superuser_permissions = Permission.objects.all()

    staff_group.permissions.set(staff_permissions)
    superuser_group.permissions.set(superuser_permissions)