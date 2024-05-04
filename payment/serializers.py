from rest_framework import serializers

class PaymentSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    product_name = serializers.CharField(max_length=255)
    # Add more fields as needed
