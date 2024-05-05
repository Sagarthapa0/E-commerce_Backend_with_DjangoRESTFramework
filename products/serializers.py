from .models import Product
from rest_framework import serializers
from .models import Review

class ProductListSerialier(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()

    class Meta:
        model= Product
        fields='__all__'

class ProductCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        title= validated_data.get('title',None)
        description= validated_data.get('description',None)
        price= validated_data.get('price',None)
        stock_quantity= validated_data.get('stock_quantity',None)
        rating= validated_data.get('rating',None)
        image= validated_data.get('image',None)
        
        seller= validated_data.get('seller',None)
        product=Product.objects.create(
            title=title,
            description=description,
            price=price,
            stock_quantity=stock_quantity,
            rating=rating,
            image=image,
            seller=seller,
        )
        return product
    

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'comment', 'created_at']