from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class Module(models.Model):
    code =  models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=6, primary_key=True)

    def __str__(self):
        return self.name + ' (' + self.code + ') '
        

class Enrollment(models.Model):
    modules = models.ManyToManyField(Module, related_name='enrollment_modules')
    course = models.ForeignKey(Course, related_name='course_enrollment', on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class User(AbstractBaseUser):
    student_number = models.CharField(primary_key=True, unique=True, max_length=8)
    first_names = models.CharField(max_length=128)
    surname = models.CharField(max_length=64)
    USERNAME_FIELD = 'student_number' # Student number is also username
    enrollment = models.ForeignKey(Enrollment, null=True, related_name='student_enrollment', on_delete=models.SET_NULL)
    # Password field provided in AbstractBaseUser class

    def __str__(self):
        return self.first_names + ' ' + self.surname + ' (' + self.student_number + ') '
    
    # Delete own account
    def delete_self(self):
        User.objects.delete(self)


class Institution(models.Model):
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, related_name='institution_courses')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

