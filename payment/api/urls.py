

from django.conf.urls import url
from .views import AccountsRUDView, AccountsAPIView, IssuerAPIView

# csrf_exempt(

urlpatterns = [
    url(r'^accounts/$', AccountsAPIView.as_view(), name='account-create'),
    url(r'^accounts/(?P<pk>[\w-]+)/$', AccountsRUDView.as_view(), name='account-rud'),
    url(r'^issuer[/]?$', (IssuerAPIView.as_view()), name='isser_view'),
]