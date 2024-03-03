# from django.shortcuts import render


# Create your views here.
# these are just copy pasted..check it again
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import generics
from .models import Order
from .serializes import OrderSerializer

# class OrderListView(APIView):
#     def get(self, request):
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
