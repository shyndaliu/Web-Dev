from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Vacancy
from api.serializers import VacancySerializer


class VacancyListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)


class VacancyDetailAPIView(APIView):
    def get_object(self, pk=None):
        try:
            vacancy = Vacancy.objects.get(id=pk)
            return vacancy
        except Vacancy.DoesNotExist as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        vacancy = self.get_object(id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)


class VacancyTopTenAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.order_by("-salary")
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
