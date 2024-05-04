from django.shortcuts import render
from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from category.models import Category
from rest_framework import exceptions,generics

from .serializers import OrderListSerializer,OrderCreateSerializer,DeliverySerializer
from .models import Order,Delivery
# Create your views here.

class OrderCreateView(CreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderCreateSerializer

class OrderListView(ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderListSerializer

class OrderRetrieveView(RetrieveAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderListSerializer

class OrderUpdateView(UpdateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderListSerializer

class OrderDeleteView(DestroyAPIView):
    queryset=Order.objects.all()


class ProductPurchasedByBuyer(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class=OrderListSerializer
    
    def get_queryset(self):
        user = self.request.user
        qs = Order.objects.filter(buyer=user)
        return qs
    

class DeliveryListView(ListAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryCreateAPIView(generics.CreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


