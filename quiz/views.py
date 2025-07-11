from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question
from .serializers import RandomQuestionSerializer

# Create your views here.
class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter().order_by("?")[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

        # Сортирует вопросы в случайном порядке (? — специальный символ для рандомизации в Django).
        # Берет только первый элемент из случайно отсортированного списка (эквивалент LIMIT 1 в SQL).
        #
        # Результат:
        # Возвращает 1 случайный вопрос при GET-запросе к этому эндпоинту.
