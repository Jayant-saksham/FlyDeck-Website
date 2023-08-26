# courses/admin.py
from django.contrib import admin
from .models import Course, CourseCategory, Video

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor', 'language', 'bio')
    list_filter = ('instructor', 'language')
    search_fields = ('name', 'instructor__email', 'language')


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseCategory)
admin.site.register(Video)


