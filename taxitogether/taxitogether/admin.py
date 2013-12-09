# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from taxitogether.models import Duck, Settings


class DuckCreationForm(UserCreationForm):
    """
    clean_username이 Meta를 검사하지 않는 문제를 회피하기 위해
    전용 Form을 작성한다.
    """

    class Meta:
        model = Duck 
        fields = ('username', 'email', 'gender')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class DuckSettingInline(admin.TabularInline):
    model = Settings


class DuckAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Taxitogether', {'fields': ('key', 'verified', )}),
    )

    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    add_form = DuckCreationForm
    inlines = [DuckSettingInline, ]


admin.site.register(Duck, DuckAdmin)
