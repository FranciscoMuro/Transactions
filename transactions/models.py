from django.db import models
class Account(models.Model):
    proprietary = models.CharField("email of the proprietary of the account", max_length=35)

class Transaction(models.Model):
    date_transaction = models.CharField("Date of transaction", max_length=6)
    quantity = models.FloatField("Quantity of the transaction", max_length=99)
    proprietary = models.CharField("Account email of the proprietary", max_length=35)
