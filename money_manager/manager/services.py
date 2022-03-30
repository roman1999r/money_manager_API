from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


from .models import *
from .serializers import *

def get_all_transactions():
    transactions = Transaction.objects.all()
    serializer = TransactionsListSerializer(transactions, many=True)
    return serializer.data



def create_transaction(request):
    serializer = TransactionsListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)




