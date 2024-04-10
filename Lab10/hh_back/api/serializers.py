from rest_framework import serializers
from api.models import Company, Vacancy


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250)
    description = serializers.CharField()
    city = serializers.CharField(max_length=250, min_length=3)
    address = serializers.CharField()

    def create(self, data):
        inst = Company.objects.create(data)
        return inst

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.city = validated_data.get("city", instance.city)
        instance.address = validated_data.get("address", instance.address)
        instance.save()
        return instance

    def delete(self, inst):
        inst.delete()


class VacancySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250)
    description = serializers.CharField()
    salary = serializers.FloatField(allow_null=False)
    company = CompanySerializer()

    class Meta:
        model = Vacancy
        fields = ("id", "name", "description", "salary", "company")
