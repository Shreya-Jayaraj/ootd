from rest_framework import serializers
from .models import Order, OrderItem
# these are just copy pasted..check it again
class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'quantity', 'unit_price', 'total_price']

    def get_total_price(self, obj):
        return obj.quantity * obj.unit_price

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'total_price', 'created_at', 'order_items']
