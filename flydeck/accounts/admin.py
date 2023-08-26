from django.contrib import admin
from .models import StudentProfile,User


class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'birth_year')
    list_filter = ('birth_year',)
    raw_id_fields = ('user',)  


class UserAdmin(admin.ModelAdmin):
    exclude = ('password',)

admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)


