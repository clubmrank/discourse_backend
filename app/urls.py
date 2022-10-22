from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post_review', views.post_review, name="post_review")
]
