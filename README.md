
## Django REST API Exercise

    A project on REST API implementation using Django REST Framework. 

### How to run the project
Make sure all of the requirements are installed
    
    Django
    djangorestframework
    djangorestframework-jwt
    
After installing the requirements run the command:
    
    python manage.py runserver
    
To run on a specific port:
    
    python manage.py runserver 8000
    

To load money to a customer's account use this command:
    
    python manage.py load_money customer_id float-amount currency(EUR, USD)
    
    # currency is case sensitive
    
Example:
    
    python manage.py load_money 7d901219 30.0 EUR
    
For receiving requests:

    URI : /api/issuer
    Query param: json
    Method: GET
    Value:
    {
      "type": "presentment",
      "card_id": "4321LOBO",
      "transaction_id": "1234ZORRO",
      "merchant_name": "authorisation",
      "merchant_country": "US",
      "merchant_mcc": "5139",
      "billing_amount": "90.00",
      "billing_currency": "EUR",
      "transaction_amount": "100.00", 
      "transaction_currency": "USD"
    }
    
    

