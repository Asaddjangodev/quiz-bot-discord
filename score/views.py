from django.shortcuts import render
from rest_framework.views import APIView # это готовая основа для обработки запросов (GET, POST, PUT и т.д.).
from .serializers import ScoreSerializer
# Create your views here.

class UpdateScores(APIView):
    def post(self, request, format=None):
