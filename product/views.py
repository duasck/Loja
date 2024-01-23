from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import productSerializer
import json

# Create your views here.
@product_view(['GET'])
def get_products(request):
    if request.method == 'GET':
       products = product.objects.all()
       serializer = productSerializer(products, many=True)
       return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@product_view(['POST', 'GET', 'PUT', 'DELETE'])
def product(request):
    if request.method == 'POST':
        serializer = productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if resquest.method == 'GET':
        products = product.get(pk=request.data['id'])
        serializer = productSerializer(products, many=True)
        return Response(serializer.data)
    if resquest.method == 'PUT':
        products = product.get(pk=request.data['id'])
        serializer = productSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if resquest.method == 'DELETE':
        products = product.get(pk=request.data['id'])
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)