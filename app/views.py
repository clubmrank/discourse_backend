from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models, logic

# Django REST API
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

# Test
@api_view(['GET'])
def index(request):
    return Response(logic.get_all_students_as_json())

@api_view(['POST'])
def post_review(request):
    success = logic.post_review_as_json(request.data)

    if success:
        return HttpResponse("Post Success")
    else:
        return HttpResponse("Post Failed")