from django.shortcuts import render
from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from category.models import Category
from rest_framework import exceptions

from .models import Cart
from .serializers import CartListSerializer,CartCreateSerializer

# Create your views here.

class CartListView(ListAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartListSerializer

class CartCreateView(CreateAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartCreateSerializer

class CartRetrieveView(RetrieveAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartListSerializer

class CartUpdateview(UpdateAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartListSerializer


class CartDeleteView(DestroyAPIView):
    queryset=Cart.objects.all()
    