from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
import csv
from .models import Branches
from .serializers import BranchesSerializer
from django.db.models import Q
import requests
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status, permissions
from django.contrib import messages
# Create your views here.


def index(request):
    response=requests.get("http://bankssapi.herokuapp.com/api/Branches/").json()
    return render(request, "show.html",{'response':response})


def handler404(request, exception=None):
    return render(request, "404.html", {})


def handler500(request, exception=None):
    return render(request, "404.html", {})



@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def Autocomplete_API(request):
    if 'q' not in request.GET or 'limit' not in request.GET or 'offset' not in request.GET:
        return Response({'message': "Please cross check your endpoint before making request, something went wrong."}, status=status.HTTP_400_BAD_REQUEST)
    if not request.GET['limit'] or not request.GET['offset']:
        return Response({'message': "Please cross check your endpoint before making request, something went wrong."}, status=status.HTTP_400_BAD_REQUEST)
    branches = Branches.objects.filter(branch__icontains=request.GET['q']).order_by('ifsc')

    limit = int(request.GET['limit'])
    offset = int(request.GET['offset'])
    return Response({'branches': BranchesSerializer(branches[limit*offset:(limit*offset)+limit], many=True).data, 'Total count': branches.count()}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def Search_API(request):
    if 'q' not in request.GET or 'limit' not in request.GET or 'offset' not in request.GET:
        return Response({'message': "Please cross check your endpoint before making request, something went wrong."}, 
        status=status.HTTP_400_BAD_REQUEST)
    if not request.GET['limit'] or not request.GET['offset']:
        return Response({'message': "Please cross check your endpoint before making request, something went wrong."}, 
        status=status.HTTP_400_BAD_REQUEST)
    branches = Branches.objects.filter(branch__icontains=request.GET['q']).order_by('ifsc')

    limit = int(request.GET['limit'])
    offset = int(request.GET['offset'])
    return Response({'branches': BranchesSerializer(branches[limit*offset:(limit*offset)+limit], many=True).data, 'Total count': branches.count()}, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def Dynamic_url_API(request,query,lim,off):
    branches = Branches.objects.filter(branch__icontains=query).order_by('ifsc')
    limit = int(lim)
    offset = int(off)
    return Response({'branches': BranchesSerializer(branches[limit*offset:(limit*offset)+limit], many=True).data, 'Total count': branches.count()}, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def search(request):
    search_term = request.GET['query']
    if len(search_term) > 50 or len(search_term) == 0:
        bt = []

        messages.warning(
            request, 'No search result found. Please refine your query')
    else:
        bt =   Branches.objects.filter(
            (
                Q(branch__icontains= search_term) |
                Q(ifsc__icontains=search_term) |
                Q(city__icontains=search_term) |
                Q(district__icontains=search_term) |
                Q(state__icontains=search_term) |
                Q(bank_name__icontains=search_term) |
                Q(ifsc__icontains=search_term) |
                Q(address__icontains=search_term)
            )
        ).order_by('ifsc')

    params = {'bt': bt, 'query': search_term,}
    return Response({'branches': BranchesSerializer(bt, many=True).data, 'Total count': bt.count()}, status=status.HTTP_200_OK)

    