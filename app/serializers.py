from rest_framework import serializers
from .models import (
    Testimonial, Teacher, CourseCategory, Course,
    Certificate, Activity, Admission, ContactMessage
)

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    category = CourseCategorySerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):
    testimonial = TestimonialSerializer(read_only=True)
    course_name = CourseSerializer(read_only=True)

    class Meta:
        model = Certificate
        fields = "__all__"


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = "__all__"


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"
