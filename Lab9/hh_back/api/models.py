from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    city = models.CharField(max_length=250)
    address = models.TextField()

    def __str__(self):
        return f"ID: { self.id}, Name: {self.name}"

    class Meta:
        app_label = "api"
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Vacancy(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: { self.id}, Name: {self.name}, Company: {self.company.name}"

    class Meta:
        app_label = "api"
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"
