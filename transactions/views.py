from ctypes import util
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from transactions.models import Account, Transaction
import utilities.operations as util
import pandas as pd
import re

# here we read and process all the info got from the csv
def readCsv(request):
    template = "uploadCSV.html"
    if request.method == "GET":
        return render(request, template, {})
    file = request.FILES['transactioncsv']
    # check if the csv is valid
    if not file.name.endswith('.csv'):
        messages.warning(request, 'is not a csv data source')
        return render(request, template, {})
    csv = pd.read_csv(file)
    totalBalance = util.getTotalBalance(csv['Transaction'])
    averageOfTransactions = util.getAverageOfTransactions(csv['Transaction'])
    transactionByMoth = util.getTransactionByMoth(csv['Date'])
    email = request.POST.get('proprietary')
    # check if the email is valid
    if(not validEmail(email)):
        messages.warning(request, 'Email is not valid')
        return render(request, template, {})
    context = {
        'totalBalance': totalBalance,
        'averageOfTransactions': averageOfTransactions,
        'transactionByMoth': transactionByMoth.items()
    }
    template = 'email.html'
    print( saveInformation(csv, email))
    if saveInformation(csv, email):
        messages.warning(request, 'something went wrong saving the information in the database')
        return render(request, template, context)
    return render(request, template, context)

# here we save the information in the db
def saveInformation(data, email):
    for index in range (0, len(data["Date"])):
        transaction = Transaction.objects.create(date_transaction=data['Date'][index], quantity=data['Transaction'][index], proprietary=email)
    account = Account.objects.create(proprietary=email)
    if transaction and account:
        return False
    else:
        return True


# This is to verify if the email has the right syntax
def validEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, email)