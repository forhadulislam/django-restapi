import json
from decimal import Decimal
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from payment.models import Accounts, Transactions, Transfers

from .serializers import AccountsSerializer, TransactionsSerializer

Currency_Values_Today = {
        'EUR': 1.0,
        'USD': 0.9
    }

class IssuerAPIView(APIView):
    
    def get(self, request, *args, **kw):
        # Accepting get Request with json as the query parameter
        status_code = status.HTTP_400_BAD_REQUEST
        try:
            raw_data = request.GET.get('json')
            data = json.loads(raw_data)
            
            
            txtype = data['type']
            card_id = data['card_id']
            billing_amount = Decimal(data['billing_amount'])
            billing_currency = data['billing_currency']
            
            userAcc = Accounts.objects.get(id=card_id)
            
            if (userAcc.balance - userAcc.reserved) > billing_amount:
                userAcc.reserved = userAcc.reserved + billing_amount
                userAcc.save()
                newTransfer = Transfers(payee=userAcc, amount=billing_amount, currency=billing_currency, trtype="DBT", authorized=True).save()
                
                Transactions(transfer=newTransfer, trtype="DBT", description=userAcc.id).save()
                Transactions(transfer=newTransfer, trtype="CDT", description="Issuer").save()
                
                status_code = status.HTTP_200_OK
            else:
                status_code = status.HTTP_403_FORBIDDEN
                
        except:
            status_code = status.HTTP_404_NOT_FOUND
        
        return Response(status=status_code)
        


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
    