from rest_framework import serializers, viewsets
from products.models import Category, Product

from .serializers import CategorySerializer, ProductSerailizer

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer 

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('category_id')
    serializers_class =  ProductSerailizer