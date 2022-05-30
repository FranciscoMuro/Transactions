from django.contrib import admin
from transactions.models import Account, Transaction


admin.site.register(Transaction)
admin.site.register(Account)