from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.db.models import Sum

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
        queryset = SuperMarketSales.objects.values('branch', 'branch__name')\
            .annotate(quantity=Sum('quantity'))

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)