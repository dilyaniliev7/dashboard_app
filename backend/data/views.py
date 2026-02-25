from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.db.models import Sum, F, Func, Value, FloatField, IntegerField, Case, When
from django.db.models.functions import Cast

class SuperMarketSalesViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = SuperMarketSales.objects.all()
    serializer_class = SuperMarketSalesSerializer

    def list(self, request):
        queryset = SuperMarketSales.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class BranchDataViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = SuperMarketSales.objects.all()
    serializer_class = ProductBranchDataSerializer

    def list(self, request):
        total_sum = SuperMarketSales.objects.aggregate(total_quantity=Sum('quantity'))
        total_quantity_value = total_sum['total_quantity']
        queryset = SuperMarketSales.objects.values('branch', 'branch__name')\
            .annotate(quantity=Sum('quantity'))\
            .annotate(percentage=Func(
            (Cast(F('quantity'), FloatField()) / total_quantity_value) * 100,
            Value(2),
            function='ROUND',
            output_field=FloatField()
        ))

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class GenderDataViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = SuperMarketSales.objects.all()
    serializer_class = GenderDataSerializer

    def list(self, request):
        queryset = SuperMarketSales.objects.values('gender', 'gender__name')\
            .annotate(quantity=Sum('quantity'))

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ProductBranchDataViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = SuperMarketSales.objects.all()
    serializer_class = ProductBranchDataSerializer

    def list(self, request):
        queryset = SuperMarketSales.objects.values('productline__name', 'gender__name')\
            .annotate(quantityBranchA=Sum(
            Case(
                When(branch__name="A", then='quantity'),
                default=0,
                output_field=IntegerField()
            )
        )) \
            .annotate(quantityBranchB=Sum(
            Case(
                When(branch__name="B", then='quantity'),
                default=0,
                output_field=IntegerField()
            )
        )) \
            .annotate(quantityBranchC=Sum(
            Case(
                When(branch__name="C", then='quantity'),
                default=0,
                output_field=IntegerField()
            )
        ))
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class CountryDataViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = SuperMarketSales.objects.all()
    serializer_class = CountryDataSerializer

    def list(self, request):
        queryset = SuperMarketSales.objects.values('date__month')\
            .annotate(quantityNetherlands=Sum(
            Case(
                When(country__name="Netherlands", then='quantity'),
                default=0,
                output_field=IntegerField()
            )
        )) \
            .annotate(quantityGermany=Sum(
            Case(
                When(country__name="Germany", then='quantity'),
                default=0,
                output_field=IntegerField()
            )
        )) \
            .annotate(quantityFrancey=Sum(
            Case(
                When(country__name="France", then='quantity'),
                default=0,
                output_field=IntegerField()
            )
        ))
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
