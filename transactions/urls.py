from django.urls import path
from .views import (readCsv)

app_name = 'autobuses'

urlpatterns = [
    path('',readCsv, name='readCsv'),
]
