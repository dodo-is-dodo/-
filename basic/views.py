from django.shortcuts import render
# from basic.serializers import UserSerializer, StoreSerializer, Query_param, ReturnSerializer
from basic.serializers import SearchSerializer, ResultSerializer
from basic.models import Store
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def transform(name):
    p = ["코카콜라", "미에로 화이바", "핫식스", "새우깡", "누드 빼빼로"]
    for i in range(len(p)):
        if name == p[i]:
            return i
    return 5

class SearchAPI(APIView):
    def get(self, request, format=None):
        serializer = SearchSerializer(data=request.data)
        print("suck")
        if serializer.is_valid():
            # print(serializer.data)
            items = serializer.data["item"]
            # print(items)
            store_list = []
            stores = Store.objects.all()
            # print("stores",stores)
            for store in stores:
                # print(store)
                total = 0
                product_list = []
                for item in items:
                    # print(item)
                    name = item["pid"]
                    print(name)
                    price = store.inventory[name]
                    volume = item["volume"]
                    pid = volume
                    total += price * volume
                    product_list.append(Product(name, pid, price))
                name = store.name
                lat = store.lat
                lon = store.lon
                store_list.append(StoreObj(name, total, lat, lon, product_list))
            result = Result(store_list)
            ret = ResultSerializer(result)
            return Response(ret.data, status=status.HTTP_200_OK)
        print("fuck")
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = SearchSerializer(data=request.data)
        print("suck")
        if serializer.is_valid():
            items = serializer.data["item"]
            store_list = []
            item_list = []
            stores = Store.objects.all()
            for store in stores:
                total = 0
                product_list = []
                for item in items:
                    name = item["pid"]
                    if name not in item_list:
                        item_list.append(name)
                    # print(name)
                    pid = transform(name)
                    price = store.inventory[name]
                    volume = item["volume"]
                    total += price * volume
                    product_list.append(Product(name, pid, price))
                name = store.name
                lat = store.lat
                lon = store.lon
                store_list.append(StoreObj(name, total, lat, lon, product_list))
            ret = getItem()
            result = Result(store_list)
            ret = ResultSerializer(result)
            return Response(ret.data, status=status.HTTP_200_OK)
        print("fuck")
        return Response(None, status=status.HTTP_400_BAD_REQUEST)


class Item:
    def __init__(self, pid, volume):
        self.pid = pid
        self.volume = volume

class Search:
    def __init__(self, item):
        self.item = item

class Product:
    def __init__(self, name, pid, price):
        self.name = name
        self.pid = pid
        self.price = price


class StoreObj:
    def __init__(self, name, total, lat, lon, product):
        self.name = name
        self.total = total
        self.lat = lat
        self.lon = lon
        self.product = product

class Result:
    def __init__(self, store):
        self.store = store
