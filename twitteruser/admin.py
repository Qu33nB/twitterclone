from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from twitteruser.models import CustomUser
from authentication.forms import SignUpForm
# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    add_form = SignUpForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('display_name', 'homepage', 'age')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('display_name','homepage', 'age',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('display_name', 'homepage', 'password1', 'password2'),
        }),
    )
    search_fields = ('display_name',)
    ordering = ('display_name',)
    filter_horizontal = ()

admin.site.register(CustomUser, UserAdmin)
