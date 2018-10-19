

from django.conf.urls import url

from .views import AccountsRUDView, AccountsAPIView

urlpatterns = [
    url(r'^accounts/$', AccountsAPIView.as_view(), name='account-create'),
    url(r'^accounts/(?P<pk>[\w-]+)/$', AccountsRUDView.as_view(), name='account-rud'),
]