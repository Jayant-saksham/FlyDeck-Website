from django.contrib import admin
from .models import StudentProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'birth_year')
    list_filter = ('birth_year',)
    raw_id_fields = ('user',)  