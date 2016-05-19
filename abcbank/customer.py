from account import CHECKING, SAVINGS, MAXI_SAVINGS, Account
from transaction import Transaction


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def openAccount(self, account):
        if isinstance(account, Account):
            self.accounts[account.accountType] = account
        elif isinstance(account, int):
            self.accounts[account] = Account(account)
        return self

    def transfer(self, fromAccount, toAccount, amount):
        if fromAccount not in self.accounts or toAccount not in self.accounts:
            return "Invalid Account"
        _from = self.accounts[fromAccount]
        _to = self.accounts[toAccount]
        if _from.availableBalance < 0 or amount > _from.availableBalance:
            return "Account does not have sufficient balance"
        _from.availableBalance -= amount
        _to.availableBalance += amount
        _from.transactions.append(Transaction(-amount))
        _to.transactions.append(Transaction(amount))
        return "Transfer Succeeded"

    def numAccs(self):
        return len(self.accounts)

    def totalInterestEarned(self):
        return sum([self.accounts[accountType].interestEarned() for accountType in self.accounts.keys()])

    # This method gets a statement
    def getStatement(self):
        # JIRA-123 Change by Joe Bloggs 29/7/1988 start
        statement = None  # reset statement to null here
        # JIRA-123 Change by Joe Bloggs 29/7/1988 end
        totalAcrossAllAccounts = sum(
            [self.accounts[accountType].sumTransactions() for accountType in self.accounts.keys()])
        statement = "Statement for %s" % self.name
        for accountType in self.accounts.keys():
            statement += self.statementForAccount(self.accounts[accountType])
        statement = statement + "\n\nTotal In All Accounts " + _toDollars(totalAcrossAllAccounts)
        return statement

    def statementForAccount(self, account):
        accountType = "\n\n\n"
        if account.accountType == CHECKING:
            accountType = "\n\nChecking Account\n"
        if account.accountType == SAVINGS:
            accountType = "\n\nSavings Account\n"
        if account.accountType == MAXI_SAVINGS:
            accountType = "\n\nMaxi Savings Account\n"
        transactionSummary = [self.withdrawalOrDepositText(t) + " " + _toDollars(abs(t.amount))
                              for t in account.transactions]
        transactionSummary = "  " + "\n  ".join(transactionSummary) + "\n"
        totalSummary = "Total " + _toDollars(sum([t.amount for t in account.transactions]))
        return accountType + transactionSummary + totalSummary

    def withdrawalOrDepositText(self, transaction):
        if transaction.amount < 0:
            return "withdrawal"
        elif transaction.amount > 0:
            return "deposit"
        else:
            return "N/A"


def _toDollars(number):
    return "${:1.2f}".format(number)
