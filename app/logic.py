from . import models
from . import serializers

from rest_framework.response import Response
from rest_framework import status

# Get one student serialised
def get_student(student_number):
    user = models.User.objects.get(pk=str(student_number))
    serialised_user = serializers.UserSerializer(user)
    return serialised_user.data


# Get a list of all students
def get_all_students():
    users = models.User.objects.all()
    serialized_users = serializers.UserSerializer(users, many=True)
    return Response(serialized_users.data)


# Get a list of all reviews
def get_all_reviews():
    reviews = models.Review.objects.all()
    serialized_reviews = serializers.ReviewSerializer(reviews, many=True)
    return Response(serialized_reviews.data)


# Get a list of all tags
def get_all_tags():
    tags = models.Tag.objects.all()
    serialized_tags = serializers.TagSerializer(tags, many=True)
    return Response(serialized_tags.data)


# Get a list of all modules
def get_all_modules():
    modules = models.Module.objects.all()
    serialized_modules = serializers.ModuleSerializer(modules, many=True)
    return Response(serialized_modules.data)


# Get a list of all courses
def get_all_courses():
    courses = models.Course.objects.all()
    serialized_courses = serializers.CourseSerializer(courses, many=True)
    return Response(serialized_courses.data)


# Get a list of all enrollments
def get_all_enrollments():
    enrollments = models.Enrollment.objects.all()
    serialized_enrollments = serializers.EnrollmentSerializer(enrollments, many=True)
    return Response(serialized_enrollments.data)


# Get a list of all institutions
def get_all_institutions():
    institutions = models.Institution.objects.all()
    serialized_institutions = serializers.InstitutionSerializer(institutions, many=True)
    return Response(serialized_institutions.data)


# Review posting code
def post_review(data):
    serialised_review = serializers.ReviewSerializer(data=data)
    if serialised_review.is_valid():
        serialised_review.save()
        return Response(serialised_review.data, status=status.HTTP_201_CREATED)

    return Response(serialised_review.errors, status=status.HTTP_400_BAD_REQUEST)