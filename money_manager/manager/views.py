from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from manager.serializers import TransactionsListSerializer
from manager.models import Transaction, Category
from .services import *

# Create your views here.
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def transactionListView(request):
    if request.method == "GET":
        all = get_all_transactions()
        return Response(all)


def create_transaction(request):
    if request.method == "POST":
        create = create_transaction(request)
    return JsonResponse(status=400, data={"message": "error"})

'''
@api_view(['POST'])
def create_transaction(request):
    if request.method == "POST":
        serializer = TransactionsListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)





@api_view(['POST'])
def create_transactionView(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TransactionsListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



class TransactionListView(ListAPIView):
    model = Transaction
    serializer_class = TransactionsListSerializer
    queryset = Transaction.objects.all()


class TransactionListView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionsListSerializer(transactions,many=True)
        return Response(serializer.data)
'''

class CreateTransactionView(CreateAPIView):
    serializer_class = TransactionsListSerializer


