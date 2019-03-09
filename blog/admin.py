from django.contrib import admin
from .models import Post, RegistroActividad

admin.site.register(Post)

@admin.register(RegistroActividad)
class RegistroActividadAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'ip','fecha']
    list_filter = ['fecha',]