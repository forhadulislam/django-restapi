from rest_framework import generics

from payment.models import Accounts, Transactions, Transfers

from .serializers import AccountsSerializer, TransactionsSerializer

class IssuerAPIView(generics.CreateAPIView):
    
    pass


class AccountsAPIView(generics.CreateAPIView):
    
    lookup_field = 'pk'
    serializer_class = AccountsSerializer
    queryset = Accounts.objects.all()
    
    def get_queryset(self):
        return Accounts.objects.all()
    

class AccountsRUDView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'pk'
    serializer_class = AccountsSerializer
    queryset = Accounts.objects.all()
    
    def get_queryset(self):
        return Accounts.objects.all()
    