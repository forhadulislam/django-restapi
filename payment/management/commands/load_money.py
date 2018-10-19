from django.core.management.base import BaseCommand
from django.utils import timezone
from payment.models import Accounts, Transactions, Transfers
from decimal import Decimal

class Command(BaseCommand):
    help = 'Loads money to a specific account'
    
    def add_arguments(self, parser):
        parser.add_argument('cardholder', type=str, help='The id of the cardholder')
        parser.add_argument('amount', type=float, help='The amount of the money')
        parser.add_argument('currency', type=str, help='The currency of the money')

    def handle(self, *args, **kwargs):
        cardholder = kwargs['cardholder']
        amount = kwargs['amount']
        currency = kwargs['currency']
        
        try:
            usedData = Accounts.objects.get(id=cardholder)
            if usedData.currency == currency:
                updatedAmount = Decimal(usedData.balance) + Decimal(amount)
                
                data_dict = {'balance': updatedAmount}
                Accounts.objects.filter(id=cardholder).update(**data_dict)
            
                self.stdout.write("Deposited {0} {1} to account #{2}".format(amount, currency, cardholder))
            else:
                self.stdout.write("The account do accept the currency given")
        except:
            self.stdout.write("Error occured! Check the input and try again")