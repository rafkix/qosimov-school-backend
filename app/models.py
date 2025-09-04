from django.db import models

# Create your models here.
class Testimonial(models.Model):
    student_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="testimonials/")
    feedback = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)  # 1 dan 5 gacha
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} ({self.rating}⭐)"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to="teachers/")
    video_url = models.URLField(blank=True, null=True)
    experience_years = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class CourseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name="courses")
    duration_weeks = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    testimonial = models.ForeignKey(
        Testimonial,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="certificates"
    )
    course_name = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="certificates"
    )
    certificate_file = models.FileField(upload_to="certificates/")
    issued_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.testimonial.student_name} - {self.course_name}"
    
class Activity(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="activities/")
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Admission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("approved", "Approved"), ("rejected", "Rejected")],
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
