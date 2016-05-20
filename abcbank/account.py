from abcbank.date_provider import DateUtils
from abcbank.transaction import Transaction

CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2


class Account:
    def __init__(self, accountType):
        self.accountType = accountType
        self.transactions = []
        self.availableBalance = 0

    def deposit(self, amount, date_deposited=None):
        """

        :param amount: amount to be deposited
        :param date_deposited: optional param; date of deposit
        :return:
        """
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        else:
            if date_deposited:
                try:
                    date = DateUtils.toDate(date_deposited)
                    self.transactions.append(Transaction(amount, date))
                except ValueError:
                    return ValueError("Incorrect date format")
            else:
                self.transactions.append(Transaction(amount))
            self.availableBalance += amount

    def withdraw(self, amount):
        """

        :param amount: amount to be withdrawn
        :return: None
        """
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        elif amount > self.availableBalance:
            raise ValueError("amount greater than available balance")
        else:
            self.transactions.append(Transaction(-amount))
            self.availableBalance -= amount

    def interestEarned(self):
        """
        calculate the interest annually

        :return: interest payout for the customer
        """
        amount = self.availableBalance
        if self.accountType == SAVINGS:
            if amount <= 1000:
                return amount * 0.001
            else:
                return 1 + (amount - 1000) * 0.002
        if self.accountType == MAXI_SAVINGS:
            endDate = DateUtils.now()
            startDate = DateUtils.add(endDate, -10)
            _transactions = self.getTransaction(startDate, endDate)
            withdrawn = 0
            for t in _transactions:
                if t.amount < 0:
                    withdrawn = 1
                    break
            if withdrawn == 1:
                return amount * (0.1 / 100.0)
            else:
                return amount * (5 / 100.0)
        else:
            return amount * 0.001

    def interest_earned_after_x_days(self, days=1):
        """
        Calculate the interest after x days

        :param days:
        :return: return the Amount along with accrued interest
        """
        amount = self.availableBalance
        if self.accountType == SAVINGS:
            if amount <= 1000:
                return Account.daily_interest(amount, 0.1, days)
            else:
                return Account.daily_interest(amount - 1000, 0.2, days) + Account.daily_interest(1000, 0.1, days)
        if self.accountType == MAXI_SAVINGS:
            endDate = DateUtils.now()
            startDate = DateUtils.add(endDate, -10)
            _transactions = self.getTransaction(startDate, endDate)
            withdrawn = 0
            for t in _transactions:
                if t.amount < 0:
                    withdrawn = 1
                    break
            if withdrawn == 1:
                return Account.daily_interest(amount, 0.1, days)
            else:
                return Account.daily_interest(amount, 5, days)
        else:
            return Account.daily_interest(amount, 0.1, days)

    def sumTransactions(self, checkAllTransactions=True):
        """

        :param checkAllTransactions:
        :return: Return the sum of all transaction including debits and credits
        """
        return sum([t.amount for t in self.transactions])

    def getTransaction(self, startDate, endDate):
        """
        Get the Customer Transaction between any time frame

        :param startDate: Start Date
        :param endDate: End Date
        :return: List of Transaction between the start date and end date
        """
        transaction_data = []
        try:
            start_date = DateUtils.toDate(startDate)
            end_date = DateUtils.toDate(endDate)
        except ValueError:
            return ValueError("Incorrect date format")
        for transaction in self.transactions:
            if DateUtils.isDateWithinRange(transaction.transactionDate, startDate, endDate):
                transaction_data.append(transaction)
        return transaction_data

    @staticmethod
    def daily_interest(P, r, days):
        """
        Calculate the Daily/Continuous Interest

        :param P: Prinicipal Amount
        :param r: Rate of Interest
        :param days: No. of days upto which the interest is calculated
        :return: Final amount with Interest accrued daily
        """
        I = P
        for x in range(days):
            I *= 1 + ((r / 100.0) / 365.0)
        return round(I, 2)

