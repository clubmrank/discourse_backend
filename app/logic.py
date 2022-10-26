from . import models
from . import serializers

from rest_framework.response import Response
from rest_framework import status

###########################################################
# Get one 
###########################################################
# Get one student
def get_student_by_id(student):
    user = models.User.objects.get(pk=str(student))
    serialized_user = serializers.UserSerializer(user)
    return Response(serialized_user.data)


# Get one module
def get_module_by_id(module):
    module = models.Module.objects.get(pk=module)
    serialized_module = serializers.ModuleSerializer(module)
    return Response(serialized_module.data)


# Get one review
def get_review_by_id(review):
    review = models.Review.objects.get(pk=review)
    serialized_review = serializers.ReviewSerializer(review)
    return Response(serialized_review.data)


# Get one tag
def get_tag_by_id(tag):
    tag = models.Tag.objects.get(pk=tag)
    serialized_tag = serializers.TagSerializer(tag)
    return Response(serialized_tag.data)


# Get one course
def get_course_by_id(course):
    course = models.Course.objects.get(pk=course)
    serialized_course = serializers.CourseSerializer(course)
    return Response(serialized_course.data)


# Get one enrollment
def get_enrollment_by_id(enrollment):
    enrollment = models.Enrollment.objects.get(pk=enrollment)
    serialized_enrollment = serializers.EnrollmentSerializer(enrollment)
    return Response(serialized_enrollment.data)


# Get one institution
def get_institution_by_id(institution):
    institution = models.Institution.objects.get(pk=institution)
    serialized_institution = serializers.InstitutionSerializer(institution)
    return Response(serialized_institution.data)


###########################################################
# Get all
###########################################################

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
    
###########################################################
# Get filtered list
###########################################################

# Get a list of all reviews by module
def get_all_reviews_by_module(module):
    module_reviews = models.Review.objects.filter(module=module)
    serialized_module_reviews = serializers.ReviewSerializer(module_reviews, many=True)
    return Response(serialized_module_reviews.data)


# Get a list of all courses by university
def get_all_courses_by_institution(institution):
    institution_courses = models.Institution.objects.get(pk=institution).courses
    serialized_courses = serializers.CourseSerializer(institution_courses, many=True)
    return Response(serialized_courses.data)


# Get a list of all modules by course
def get_all_modules_by_course(course):
    course_modules = models.Course.objects.get(pk=course).modules
    serialized_modules = serializers.ModuleSerializer(course_modules, many=True)
    return Response(serialized_modules.data)

###########################################################
# Post
###########################################################

# Post a review
def post_review(data):
    serialised_review = serializers.ReviewSerializer(data=data)
    if serialised_review.is_valid():
        serialised_review.save()
        return Response(serialised_review.data, status=status.HTTP_201_CREATED)

    return Response(serialised_review.errors, status=status.HTTP_400_BAD_REQUEST)