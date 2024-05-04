from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import Category
from .serializers import CategoryListSerialier,CategoryCreateSerializer

# Create your views here.

class CategoryCreateView(CreateAPIView):
    queryset= Category.objects.all()
    serializer_class=CategoryCreateSerializer
    # authentication_classes = [IsAuthenticated]
    # permission_classes = [TokenAuthentication]

class CreateCategoryView(CreateAPIView):
    # queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer

class CategoryListView(ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategoryListSerialier

class CategoryRetrieveView(RetrieveAPIView):
    authentication_classes = [IsAuthenticated]
    permission_classes = [TokenAuthentication]
    
    queryset=Category.objects.all()
    serializer_class=CategoryListSerialier

class CategoryUpdateView(UpdateAPIView):
    authentication_classes = [IsAuthenticated]
    permission_classes = [TokenAuthentication]

    queryset=Category.objects.all()
    serializer_class=CategoryListSerialier

class CategoryDeleteView(DestroyAPIView):
    authentication_classes = [IsAuthenticated]
    permission_classes = [TokenAuthentication]

    queryset=Category.objects.all()



