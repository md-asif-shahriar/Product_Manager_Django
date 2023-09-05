from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ProductCategoryModel
from .serializers import ProductCategoryModelSerializer

# Create your views here.


def home(request):
    return HttpResponse('<h2>This is home</h2>')


@api_view(['GET'])
def getCategory(request):
    category = ProductCategoryModel.objects.all()
    serializer = ProductCategoryModelSerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getOneCategory(request, pk):
    category = ProductCategoryModel.objects.get(cid=pk)
    serializer = ProductCategoryModelSerializer(category, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addCategory(request):
    serializer = ProductCategoryModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# update


@api_view(['POST'])
def updateCategory(request, pk):
    prev_category = ProductCategoryModel.objects.get(cid=pk)
    serializer = ProductCategoryModelSerializer(
        instance=prev_category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteCategory(request, pk):
    category = ProductCategoryModel.objects.get(cid=pk)
    category.delete()
    return Response("Product Category deleted successfully!")
