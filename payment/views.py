from django.shortcuts import render

# Create your views here.
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PaymentSerializer
from django.conf import settings

class PaymentAPIView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment_data = serializer.validated_data
            url = 'https://khalti.com/api/v2/payment/verify/'
            payload = {
                'token': payment_data.get('token'),
                'amount': payment_data.get('amount')
            }
            headers = {
                'Authorization': f"Key {settings.KHALTI_SECRET_KEY}"
            }
            response = requests.post(url, json=payload, headers=headers)
            data = response.json()
            if data['state']['name'] == 'Completed':
                return Response({'message': 'Payment successful', 'transaction_id': data['idx']}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Payment failed'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
