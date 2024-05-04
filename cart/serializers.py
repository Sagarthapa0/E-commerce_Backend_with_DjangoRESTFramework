from rest_framework import serializers
from .models import Cart


class CartListSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=True)
    user = serializers.StringRelatedField()
    class Meta:
        model = Cart
        fields = "__all__"


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

    
    def create(self, validated_data):
        products = validated_data.pop('product',None)
        total = 0
        for product in products:
            total = total + product.price
        # total= validated_data.get('total',None)
        product= validated_data.get('product',None)
        user= validated_data.get('user',None)
        quantity= validated_data.get('quantity',None)
        
        cart=Cart.objects.create(
            
            user=user,          
            quantity=quantity,           
        )
        cart.product.set(products)
        cart.save()
        return cart
    
