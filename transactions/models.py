from django.db import models

class Transaction(models.Model):
    date_transaction = models.DateField()
    cuantity = models.CharField("Cuantity of the transaction", max_length=99)
    type = models.CharField("Type of the transaction", max_length=99)