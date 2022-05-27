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
        messages.error(request, 'is not a csv data source')
    csv = pd.read_csv(file)
    totalBalance = util.getTotalBalance(csv['Transaction'])
    averageOfTransactions = util.getAverageOfTransactions(csv['Transaction'])
    transactionByMoth = util.getTransactionByMoth(csv['Date'])
    return render(request, template, {})


