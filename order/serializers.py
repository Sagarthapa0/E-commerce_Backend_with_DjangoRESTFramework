from rest_framework import serializers
from .models import Order,Delivery



class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    delivery = DeliverySerializer()
    product = serializers.StringRelatedField(many=True)
    buyer = serializers.StringRelatedField()

    class Meta:
        model=Order
        fields= "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):  
     

    class Meta:
        model = Order
        fields=['product','buyer','is_ordered','date_ordered','quantity']

    def create(self, validated_data):
        products = validated_data.pop('product',None)
        total = 0
        for product in products:
            total = total + product.price
        # total= validated_data.get('total',None)
        buyer= validated_data.get('buyer',None)
        is_ordered= validated_data.get('is_ordered',None)
        date_ordered= validated_data.get('date_ordered',None)
        quantity= validated_data.get('quantity',None)
        
        order=Order.objects.create(
            total=total,
            buyer=buyer,
            is_ordered=is_ordered,
            date_ordered=date_ordered,           
            quantity=quantity,           
        )
        order.product.set(products)
        order.save()

        
        return order
    
    