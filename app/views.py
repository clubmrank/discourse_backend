from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models, logic, serializers

# Django REST API
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

# Test
@api_view(['GET'])
def index(request):
    return logic.get_all_tags()

@api_view(['POST'])
def post_review(request):
    return logic.post_review(request.POST)