#_________________________________________________________________________  ACCOUNTS/ADMIN.PY
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html


#___________________________________________________________  CLASS ACCOUNTADMIN
class AccountAdmin(UserAdmin):
      '''
      Custom admin configuration for the Account model.
      '''
      list_display       = ('email','first_name','last_name','username','last_login','date_joined','is_active')
      list_display_links = ('email','first_name','last_name')
      readonly_fields    = ('last_login', 'date_joined')
      ordering           = ('-date_joined',)

      # Added due to custom class
      filter_horizontal  = ()
      list_filter        = ()
      fieldsets          = ()


#___________________________________________________________  CLASS USERPROFILEADMIN
class UserProfileAdmin(admin.ModelAdmin):
      '''
      Custom admin configuration for the UserProfile model.
      '''
      def thumbnail(self, object):
            return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
      thumbnail.short_description = 'Profile Picture'
      list_display = ('thumbnail','user','city','country')


admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile,UserProfileAdmin)