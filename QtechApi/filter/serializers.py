from rest_framework import serializers
from .models import Brand, Seller, Category, Product

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    seller = SellerSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
