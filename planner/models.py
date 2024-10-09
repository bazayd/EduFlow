from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    SCHOOL_PATHS = [
    ("UD", "Undergrad"),
    ("AS", "Associates"),
    ("GR", "Graduate"),
    ("PHD", "Doctorate"),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    school_path  = models.CharField(max_length=3, choices=SCHOOL_PATHS)
    enrollment_year = models.IntegerField()
    major = models.CharField(max_length=30)

