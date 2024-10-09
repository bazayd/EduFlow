from django.contrib import admin
from .models import Student, User # Ensure this is correct

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'school_path', 'enrollment_year', 'major')
