from rest_framework import serializers

from payment.models import Accounts, Transactions, Transfers

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = [
                'id',
                'balance',
                'reserved',
                'currency',
            ]
            
        read_only_fields = [
                'id'
            ]
            
class TransfersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfers
        fields = [
                'id',
                'transfer',
                'amount',
                'currency',
                'trtype',
                'amount',
                'timestamp',
            ]
            
        read_only_fields = [
                'id'
            ]
            
class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = [
                'id',
                'transfer',
                'trtype',
                'description',
                'timestamp',
            ]
            
        read_only_fields = [
                'id'
            ]
            