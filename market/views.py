from django.shortcuts import render

from .serializers import ProductsSerializer
from .models import Products

from rest_framework.views import APIView
from rest_framework.response import Response


class ProductListView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response({"result": serializer.data})
