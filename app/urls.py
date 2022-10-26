from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "app"

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('login', LoginView.as_view(template_name='app/login.html'), name="login"),

    ###########################################################
    # Get one 
    ###########################################################
    path('get_student_by_id/<str:student_id>', views.get_student_by_id, name="get_student_by_id"),
    path('get_module_by_id/<str:module_id>', views.get_module_by_id, name="get_module_by_id"),
    path('get_review_by_id/<str:review_id>', views.get_review_by_id, name="get_review_by_id"),
    path('get_course_by_id/<str:course_id>', views.get_course_by_id, name="get_course_by_id"),
    path('get_tag_by_id/<str:tag_id>', views.get_tag_by_id, name="get_tag_by_id"),
    path('get_institution_by_id/<str:institution_id>', views.get_institution_by_id, name="get_institution_by_id"),
    path('get_enrollment_by_id/<str:enrollment_id>', views.get_enrollment_by_id, name="get_enrollment_by_id"),

    ###########################################################
    # Get all
    ###########################################################
    path('get_all_institutions/', views.get_all_institutions, name="get_all_institutions"),
    path('get_all_courses', views.get_all_courses, name="get_all_courses"),
    path('get_all_modules', views.get_all_modules, name="get_all_modules"),
    path('get_all_reviews', views.get_all_reviews, name="get_all_reviews"),
    path('get_all_tags', views.get_all_tags, name="get_all_tags"),
    path('get_all_students', views.get_all_students, name="get_all_students"),
    path('get_all_enrollments', views.get_all_enrollments, name="get_all_enrollments"),

    ###########################################################
    # Get filtered list
    ###########################################################
    path('get_all_courses_by_institution/<int:institution_id>', views.get_all_courses_by_institution, name="get_all_courses_by_institution"),
    path('get_all_modules_by_course/<str:course_id>', views.get_all_modules_by_course, name="get_all_modules_by_course"),
    path('get_all_reviews_by_module/<str:module_id>', views.get_all_reviews_by_module, name="get_all_reviews_by_module"),

    ###########################################################
    # Post
    ###########################################################
    path('post_review', views.post_review, name="post_review"),
]
