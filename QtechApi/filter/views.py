from django.db.models import Q
from rest_framework import generics
from .models import Product,Seller,Category,Brand
from .serializers import ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        # Apply filters based on query parameters
        brand = self.request.query_params.get('brand')
        if brand:
            queryset = queryset.filter(brand__name=brand)

        seller = self.request.query_params.get('seller')
        if seller:
            queryset = queryset.filter(seller__name=seller)

        warranty = self.request.query_params.get('warranty')
        if warranty:
            queryset = queryset.filter(warranty=warranty)

        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price and max_price:
            queryset = queryset.filter(price__range=(min_price, max_price))
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name=category)

        return queryset
