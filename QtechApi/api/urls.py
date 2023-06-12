from django.urls import path,include
from filter.views import ProductListAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
]
