from django.contrib import admin
from .models import Profile, CustomUser

admin.site.register(Profile)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name', 'phone','is_active']
    list_filter = ['username',]