
from datetime import datetime
from numpy import average
from collections import Counter
# here we get the total transaction only by making the sum of all the array
def getTotalBalance(transactions):
    total = 0
    for transaction in transactions:
        total = transaction + total
    return total

#  here we get the average of the type of the transaction with help of numpy function.
def getAverageOfTransactions(transactions):
    typeTransactions = getTypeOfTransaction(transactions)
    averageOfTransactions = {
        'debit': average(typeTransactions.get('debit')),
        'credit': average(typeTransactions.get('credit'))
    }
    return averageOfTransactions

# here we make the distinction of the type of the transaction only by the - symbol
def isDebit(quantity):
    identifier = str(quantity)[0]
    if identifier == '-':
        return True
    return False

# here we make separated arrays for each transaction
def getTypeOfTransaction(transactions):
    debit = []
    credit = []
    for transaction in transactions:
        # here we call the function to make the distinction fo the type of transaction
        if isDebit(transaction):
            debit.append(transaction)
        else:
            credit.append(transaction)
    return {
        'debit': debit,
        'credit': credit
    }

# here we get the times a transaction was made by month
def getTransactionByMoth(dates):
    datesArray = []
    for date in dates:
        # this is just to get the name of the month base in his number
        month = datetime.strptime(date.split('/')[0], '%m')
        datesArray.append(month.strftime('%B'))
    # we use counter to get the times of a string appear in the array
    return Counter(datesArray)