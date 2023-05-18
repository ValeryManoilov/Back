from django.contrib import admin
from Ed_app.models import CourseInfo

@admin.register(CourseInfo)
class CourseInfoAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'price']