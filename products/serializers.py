from products.models import Category, Product
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fileds = '__all__'

class ProductSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fileds = '__all__'


