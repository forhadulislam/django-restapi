from django.core.management.base import BaseCommand
from django.utils import timezone

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
        
        self.stdout.write("Deposited {0} {1} to account #{2}".format(amount, currency, cardholder))