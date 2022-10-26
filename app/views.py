from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from . import logic, models, forms

# Authentication

# Django REST API
from rest_framework.decorators import api_view

# Create your views here.

def signup(request):
    if request.method == 'POST':
        new_user = forms.UserSignupForm(request.POST)
        if new_user.is_valid():
            first_names = new_user.cleaned_data.get('first_names')
            surname = new_user.cleaned_data.get('surname')
            student_number = new_user.cleaned_data.get('student_number')
            password = new_user.cleaned_data.get('password')

            try:
                user = models.User.objects.create(first_names=first_names, surname=surname, student_number=student_number, password=password)
                user.save()
                return HttpResponse("User created")
            except IntegrityError:
                return HttpResponse("User already exists")

        return HttpResponse("User creation failed")
    return render(request, "app/signup.html")


######################################################################
# Get one
######################################################################

# Get student by id
@api_view(['GET'])
def get_student_by_id(request, student_id):
    return logic.get_student_by_id(student_id)


# Get module by id
@api_view(['GET'])
def get_module_by_id(request, module_id):
    return logic.get_module_by_id(module_id)


# Get course by id
@api_view(['GET'])
def get_course_by_id(request, course_id):
    return logic.get_course_by_id(course_id)


# Get review by id
@api_view(['GET'])
def get_review_by_id(request, review_id):
    return logic.get_review_by_id(review_id)


# Get tag by id
@api_view(['GET'])
def get_tag_by_id(request, tag_id):
    return logic.get_tag_by_id(tag_id)


# Get enrollment by id
@api_view(['GET'])
def get_enrollment_by_id(request, enrollment_id):
    return logic.get_module_by_id(enrollment_id)


# Get Institution by id
@api_view(['GET'])
def get_institution_by_id(request, institution_id):
    return logic.get_module_by_id(institution_id)

#####################################################################
# Get all
####################################################################

# Get all institutions
@api_view(['GET'])
def get_all_institutions(request):
    return logic.get_all_institutions()


# Get all courses
@api_view(['GET'])
def get_all_courses(request):
    return logic.get_all_courses()


# Get all modules
@api_view(['GET'])
def get_all_modules(request):
    return logic.get_all_modules()


# Get all tags
@api_view(['GET'])
def get_all_tags(request):
    return logic.get_all_tags()


# Get all students
@api_view(['GET'])
def get_all_students(request):
    return logic.get_all_students()


# Get all reviews
@api_view(['GET'])
def get_all_reviews(request):
    return logic.get_all_reviews()


# Get all enrollments
@api_view(['GET'])
def get_all_enrollments(request):
    return logic.get_all_enrollments()

#####################################################################
# Get filtered list
####################################################################

# Get all courses by institution
@api_view(['GET'])
def get_all_courses_by_institution(request, institution_id):
    return logic.get_all_courses_by_institution(institution_id)


# Get all modules by course
@api_view(['GET'])
def get_all_modules_by_course(request, course_id):
    return logic.get_all_modules_by_course(course_id)


# Get all reviews by module
@api_view(['GET'])
def get_all_reviews_by_module(request, module_id):
    return logic.get_all_reviews_by_module(module_id)

####################################################################
# Post
####################################################################

# Post a review
@api_view(['POST'])
def post_review(request):
    return logic.post_review(request.POST)