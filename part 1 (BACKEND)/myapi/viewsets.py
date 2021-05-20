from rest_framework import viewsets
from . import models
from . import serializers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Branches
from rest_framework import generics
from rest_framework import serializers
from .serializers import BranchesSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter



class BranchViewPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 3

class BranchesViewset(viewsets.ModelViewSet):
    queryset = models.Branches.objects.all()
    serializer_class = BranchesSerializer
    # filter_backends = (DjangoFilterBackend , SearchFilter , OrderingFilter)
    # filter_fields = ['branch']
    # search_fields = '__all__'
    # pagination_class = BranchViewPagination
    # ordering_fields = ['ifsc']




