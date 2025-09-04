# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TestimonialViewSet, TeacherViewSet, CourseCategoryViewSet, CourseViewSet,
    CertificateViewSet, ActivityViewSet, AdmissionViewSet, ContactMessageViewSet
)

router = DefaultRouter()
router.register("testimonials", TestimonialViewSet)
router.register("teachers", TeacherViewSet)
router.register("categories", CourseCategoryViewSet)
router.register("courses", CourseViewSet)
router.register("certificates", CertificateViewSet)
router.register("activities", ActivityViewSet)
router.register("admissions", AdmissionViewSet)
router.register("contacts", ContactMessageViewSet)

urlpatterns = [
    path("", include(router.urls)),  # router URLlarini shu yerda ulaymiz
]
