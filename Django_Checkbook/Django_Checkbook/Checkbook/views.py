from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Transaction
from .forms import AccountForm, TransactionForm


# Function that renders the Checkbook home page
def home(request):
    form = TransactionForm(data=request.POST or None)  # Retrieve Transaction form because it has the foreign key field
    if request.method == 'POST':
        pk = request.POST['account']  # If the form is submitted, retrieve which account the user wants to view
        return balance(request, pk)  # call balance function to render that account's Balance Sheet
    content = {'form': form}  # Pass content to the template in a dictionary
    return render(request, 'checkbook/index.html', content)


# Function that renders the Create Account page
def create_account(request):
    form = AccountForm(data=request.POST or None)  # Retrieve the Account form
    if request.method == 'POST':
        if form.is_valid():  # Check to see if the submitted form is valid and if so, saves the form
            form.save()
            return redirect('index')  # Return to the index
    content = {'form': form}  # Pass content to the template in a dictionary
    return render(request, 'checkbook/CreateNewAccount.html', content)


# Function that renders the Balance Sheet page. Takes in an account's primary key (pk)
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # Retrieve the requested account using its pk
    transactions = Transaction.Transactions.filter(account=pk)  # Retrieve all of that account's transactions
    current_total = account.initial_deposit  # Create account total variable, starting with initial deposit value
    table_contents = {}  # Create a dictionary into which transaction information will be placed
    for t in transactions:  # Loop through transactions and determine which is a deposit or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount  # If deposit add amount to balance
            table_contents.update({t: current_total})  # Add transaction and total to the dictionary
        else:
            current_total -= t.amount  # If withdrawal subtract amount from balance
            table_contents.update({t: current_total})  # Add transaction and total to the dictionary
    # Pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# Function that renders the Add Transaction page
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # Retrieve the Transaction form
    if request.method == 'POST':
        if form.is_valid():  # Check to see if the submitted form is valid and if so, saves the form
            pk = request.POST['account']  # Retrieve which account the transaction was for
            form.save()
            return balance(request, pk)  # call balance to render that account's Balance Sheet
    # Pass content to the template in a dictionary
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
