#_________________________________________________________________________  ACCOUNTS/ADMIN.PY  -->
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin): # Displays Django admin dashboard
      list_display       = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
      list_display_links = ('email', 'username', 'first_name', 'last_name')
      readonly_fields    = ('last_login', 'date_joined')
      ordering           = ('-date_joined',)

      # Added due to custom class
      filter_horizontal  = ()
      list_filter        = ()
      fieldsets          = ()

admin.site.register(Account, AccountAdmin)
