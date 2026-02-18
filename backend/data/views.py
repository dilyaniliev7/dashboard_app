from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.db.models import Sum, F, Func, Value, FloatField
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
    serializer_class = BranchDataSerializer

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