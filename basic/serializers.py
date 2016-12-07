from rest_framework import serializers
from basic.models import Store

class ItemSerializer(serializers.Serializer):
    pid = serializers.CharField()
    volume = serializers.IntegerField()

class SearchSerializer(serializers.Serializer):
    item = ItemSerializer(many=True)


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    pid = serializers.IntegerField()
    price = serializers.IntegerField()

class StoreSerializer(serializers.Serializer):
    name = serializers.CharField()
    total = serializers.IntegerField()
    lat = serializers.DecimalField(max_digits=20, decimal_places=10)
    lon = serializers.DecimalField(max_digits=20, decimal_places=10)
    product = ProductSerializer(many=True)


class ResultSerializer(serializers.Serializer):
    store = StoreSerializer(many=True)

