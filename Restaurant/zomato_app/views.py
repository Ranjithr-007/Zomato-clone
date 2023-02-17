from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Restaurant, Food, Account, Order
from .serializers import UserSerializer, FoodSerializer, OrderSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FoodList(APIView):
    def get(self, request, restaurant_id):
        foods = Food.objects.filter(restaurant=restaurant_id)
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
