from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import services


@api_view(['GET'])
def transaction_list_view(request):
    if request.method == "GET":
        transactions = services.get_all_transactions()
        return Response(transactions)


@api_view(["POST"])
def create_transaction(request):
    trans = services.create_transaction(data=request.data)
    return Response(trans)


