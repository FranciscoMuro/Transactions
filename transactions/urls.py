from django.urls import path
from .views import (readCsv)

app_name = 'transactions'

urlpatterns = [
    path('',readCsv, name='readCsv'),
]
