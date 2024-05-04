from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from category.models import Category
from rest_framework import exceptions,generics

from .models import Product,Review
from .serializers import ProductListSerialier,ProductCreateSerializer,ReviewSerializer
# Create your views here.



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