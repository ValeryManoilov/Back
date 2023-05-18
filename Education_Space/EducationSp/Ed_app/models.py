from django.db import models
from django.contrib.auth.models import User
import rest_framework

class CourseInfo(models.Model):
    course_name = models.CharField(max_length=30, unique=True)
    course_description = models.TextField()
    course_pic = models.TextField()
    price = models.CharField(max_length=10)