from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from manager.serializers import TransactionsListSerializer
from manager.models import Transaction, Category


# Create your views here.
from rest_framework.views import APIView


class TransactionListView(ListAPIView):
    model = Transaction
    serializer_class = TransactionsListSerializer
    queryset = Transaction.objects.all()

'''
class TransactionListView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionsListSerializer(transactions,many=True)
        return Response(serializer.data)
'''

class CreateTransactionView(CreateAPIView):
    serializer_class = TransactionsListSerializer


