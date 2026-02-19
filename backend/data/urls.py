from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('supermarketsales', SuperMarketSalesViewSet, basename='supermarketsales')
router.register('branchdata', BranchDataViewSet, basename='branchdata')
router.register('genderdata', GenderDataViewSet, basename='genderdata')

urlpatterns = router.urls
