from django.contrib import admin
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','age','email','address','phone_number','is_staff')
    list_filter = ('username',)



admin.site.register(CustomUser,CustomUserAdmin)
