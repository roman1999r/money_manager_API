from .serializers import *


def get_all_transactions():
    transactions = Transaction.objects.all()
    serializer = TransactionsListSerializer(transactions, many=True)
    return serializer.data


def create_transaction(data):
    serializer = TransactionsListSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return "error"




