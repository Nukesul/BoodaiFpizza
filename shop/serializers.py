from rest_framework import serializers
from .models import Branch, Category, Pizza, Order

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'address', 'phone']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, allow_null=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    branch_name = serializers.CharField(source='branch.name', read_only=True)

    class Meta:
        model = Pizza
        fields = ['id', 'name', 'category', 'category_name', 'branch', 'branch_name', 'base_price', 'description', 'image', 'stock', 'discount']

class OrderSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.name', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'address', 'branch', 'branch_name', 'delivery', 'comment', 'total', 'created_at', 'items', 'status', 'promo_code']