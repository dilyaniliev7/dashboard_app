from rest_framework import serializers
from .models import *

class SuperMarketSalesSerializer(serializers.ModelSerializer):
    gender = serializers.SlugRelatedField(
        queryset=Gender.objects.all(),
        slug_field='name'
    )

    country = serializers.SlugRelatedField(
        queryset=Country.objects.all(),
        slug_field='name'
    )

    customer_type = serializers.SlugRelatedField(
        queryset=CustomerType.objects.all(),
        slug_field='name'
    )
    branch = serializers.SlugRelatedField(
        queryset=Branch.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = SuperMarketSales
        fields = '__all__'


class BranchDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='branch')
    label = serializers.CharField(source='branch__name')
    value = serializers.IntegerField(source='quantity')