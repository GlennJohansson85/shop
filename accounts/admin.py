#_________________________________________________________________________  ACCOUNTS/ADMIN.PY  -->
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html


class AccountAdmin(UserAdmin): # Displays Django admin dashboard
      list_display       = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
      list_display_links = ('email', 'username', 'first_name', 'last_name')
      readonly_fields    = ('last_login', 'date_joined')
      ordering           = ('-date_joined',)

      # Added due to custom class
      filter_horizontal  = ()
      list_filter        = ()
      fieldsets          = ()


class UserProfileAdmin(admin.ModelAdmin):
      def thumbnail(self, object):
            return format_html('<img src="{}" width="30" style="border-radius: 50%">'.format(object.profile_picture.url))
      thumbnail.short_description = 'Profile Picture'
      list_display = ('thumbnail', 'user', 'city', 'country')


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)