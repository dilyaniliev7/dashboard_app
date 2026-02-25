from rest_framework import serializers
from .models import *
import calendar

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


class GenderDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='gender')
    label = serializers.CharField(source='gender__name')
    value = serializers.IntegerField(source='quantity')


class ProductBranchDataSerializer(serializers.Serializer):
    productline__name = serializers.CharField()
    quantityBranchA = serializers.IntegerField()
    quantityBranchB = serializers.IntegerField()
    quantityBranchC = serializers.IntegerField()


class CountryDataSerializer(serializers.Serializer):
    date__month = serializers.CharField()
    quantityNetherlands = serializers.IntegerField()
    quantityGermany= serializers.IntegerField()
    quantityFrance = serializers.IntegerField()
    month_name = serializers.SerializerMethodField()

    def get_month_name(self, obj):
        return calendar.month_name[obj['date__month']]