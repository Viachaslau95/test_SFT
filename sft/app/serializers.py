from rest_framework import serializers

from app.models import Contract, Manufacturer


class ContractSerializer(serializers.ModelSerializer):
    manufacturers = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = [
            'id',
            'title',
            'manufacturers',
        ]

    def get_manufacturers(self,instance):
        result = Manufacturer.objects.filter(products__bid__contract=instance)\
            .distinct().values('title')
        return result

