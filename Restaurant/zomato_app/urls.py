from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from zomato_app.views import UserCreate, FoodList, OrderCreate

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', UserCreate.as_view(), name='register'),
    path('restaurant/<int:restaurant_id>/food/', FoodList.as_view(), name='food-list'),
    path('order/create/', OrderCreate.as_view(), name='order-create'),
]
