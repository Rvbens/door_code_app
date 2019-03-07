from django.contrib import admin
from .models import Profile, CustomUser, AuditEntry

admin.site.register(Profile)
admin.site.register(CustomUser)

@admin.register(AuditEntry)
class AuditEntryAdmin(admin.ModelAdmin):
    list_display = ['action', 'username', 'ip','date']
    list_filter = ['date',]