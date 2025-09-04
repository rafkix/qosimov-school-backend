from django.contrib import admin
from .models import (
    Testimonial, Teacher, CourseCategory, Course,
    Certificate, Activity, Admission, ContactMessage
)

# Register your models here.

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("student_name", "rating", "created_at")
    search_fields = ("student_name", "feedback")
    list_filter = ("rating", "created_at")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "experience_years")
    search_fields = ("name", "subject")


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher")
    search_fields = ("name",)
    list_filter = ("teacher",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "teacher", "duration_weeks", "price")
    search_fields = ("title", "description")
    list_filter = ("category", "teacher")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("testimonial", "course_name", "issued_date")
    search_fields = ("testimonial__student_name", "course_name__title")
    list_filter = ("issued_date",)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    search_fields = ("title", "description")
    list_filter = ("date",)


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "course", "status", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone")
    list_filter = ("status", "course", "created_at")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    list_filter = ("created_at",)
