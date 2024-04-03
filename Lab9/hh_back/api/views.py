from .models import Company, Vacancy
from django.http import JsonResponse


def do_smth(request):
    pass


def company_list(request):
    companies = Company.objects.all()
    json = [
        {
            "id": c.id,
            "name": c.name,
            "description": c.description,
            "city": c.city,
            "address": c.address,
        }
        for c in companies
    ]
    return JsonResponse(json, safe=False)


def company_details(request, id):
    try:
        company = Company.objects.get(id=id)
        json = {
            "id": company.id,
            "name": company.name,
            "description": company.description,
            "city": company.city,
            "address": company.address,
        }
        return JsonResponse(json)
    except Company.DoesNotExist:
        return JsonResponse({"error": "Company not found"}, status=404)


def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
        vacancies = Vacancy.objects.filter(company=company)
        json = [
            {
                "id": v.id,
                "name": v.name,
                "description": v.description,
                "salary": v.salary,
                "company": v.company.id,
            }
            for v in vacancies
        ]
        return JsonResponse(json, safe=False)
    except Company.DoesNotExist:
        return JsonResponse({"error": "Company not found"}, status=404)


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    json = [
        {
            "id": v.id,
            "name": v.name,
            "description": v.description,
            "salary": v.salary,
            "company": v.company.id,
        }
        for v in vacancies
    ]
    return JsonResponse(json, safe=False)


def vacancy_detail(request, id):
    try:
        v = Vacancy.objects.get(id=id)
        json = {
            "id": v.id,
            "name": v.name,
            "description": v.description,
            "salary": v.salary,
            "company": v.company.id,
        }
        return JsonResponse(json, safe=False)
    except Vacancy.DoesNotExist:
        return JsonResponse({"error": "Vacancy not found"}, status=404)


def vacancies_top_ten(request):
    vacancies = Vacancy.objects.order_by("-salary")
    json = [
        {
            "id": v.id,
            "name": v.name,
            "description": v.description,
            "salary": v.salary,
            "company": v.company.id,
        }
        for v in vacancies
    ]
    return JsonResponse(json, safe=False)
