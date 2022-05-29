from ctypes import util
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
import pandas as pd
import utilities.operations as util

def readCsv(request):
    template = "getCSV.html"
    if request.method == "GET":
        return render(request, template, {})
    file = request.FILES['transactioncsv']
    if not file.name.endswith('.csv'):
        messages.warning(request, 'is not a csv data source')
        return render(request, template, {})
    csv = pd.read_csv(file)
    totalBalance = util.getTotalBalance(csv['Transaction'])
    averageOfTransactions = util.getAverageOfTransactions(csv['Transaction'])
    transactionByMoth = util.getTransactionByMoth(csv['Date'])
    context = {
        'totalBalance': totalBalance,
        'averageOfTransactions': averageOfTransactions,
        'transactionByMoth': transactionByMoth.items()
    }

    template = 'email.html'
    return render(request, template, context)


