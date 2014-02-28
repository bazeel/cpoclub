from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import InvitationCode, UserProfile


class InvitationCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'profile__user')

    def profile__user(self, obj):
        return obj.profile.user
    profile__user.short_description = _('user')


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'profile__invcode')
    inlines = [UserProfileInline,]

    def profile__invcode(self, obj):
        return obj.profile.invitation_code
    profile__invcode.short_description = _('invitation code')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(InvitationCode, InvitationCodeAdmin)
