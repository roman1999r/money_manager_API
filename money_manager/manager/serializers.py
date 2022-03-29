from rest_framework import serializers
from manager.models import Transaction, Category


class TransactionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


