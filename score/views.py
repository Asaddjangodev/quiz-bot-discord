from django.shortcuts import render
from rest_framework.views import APIView # это готовая основа для обработки запросов (GET, POST, PUT и т.д.).
from .serializers import ScoreSerializer
from rest_framework.response import Response
from rest_framework import status

from .models import Score
# Create your views here.

class UpdateScores(APIView):

    def post(self, request, format=None):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():

            name = serializer.validated_data['name']
            points = serializer.validated_data['points']

            if Score.objects.filter(name=name).exists():
                serializer = Score.objects.get(name=name)
                serializer.points = F('point') + points

            serializer.save()

            return Response(None, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
