from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from category.models import Category
from rest_framework import exceptions,generics

from .models import Product,Review
from .serializers import ProductListSerialier,ProductCreateSerializer,ReviewSerializer
from rest_framework.filters import SearchFilter
# Create your views here.


class ProductListSearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerialier

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title')
        category = self.request.query_params.get('category')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if category:
            queryset = queryset.filter(category__name__icontains=category)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class ProductListView(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductListSerialier
    
    


class ProductCreateView(CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductCreateSerializer

    # authentication_classes = [IsAuthenticated]
    # permission_classes = [TokenAuthentication]

class ProductRetrieveview(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductListSerialier


class ProductUpdateView(UpdateAPIView):   
    authentication_classes = [IsAuthenticated]
    permission_classes = [TokenAuthentication]

    queryset=Product.objects.all()
    serializer_class=ProductListSerialier

class ProductDeleteView(DestroyAPIView):
    authentication_classes = [IsAuthenticated]
    permission_classes = [TokenAuthentication]

    queryset=Product.objects.all()


class ProductByCategory(ListAPIView):
    serializer_class=ProductListSerialier
    queryset=Product.objects.all()

    def get_queryset(self):
        # sourcery skip: inline-immediately-returned-variable
        category_name = self.kwargs['name']
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            raise exceptions.APIException("Category not found")
        
        queryset = Product.objects.filter(category=category)
        return queryset
    









class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return Review.objects.filter(product_id=product_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]