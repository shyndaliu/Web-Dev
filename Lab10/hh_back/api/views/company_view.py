from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Company, Vacancy

from api.serializers import CompanySerializer, VacancySerializer


@api_view(["GET"])
def company_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def company_details(request, id=None):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        serializer = CompanySerializer(company)
        return Response(serializer.data)


@api_view(["GET"])
def company_vacancies(request, id=None):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        vacancies = Vacancy.objects.filter(company=company)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
