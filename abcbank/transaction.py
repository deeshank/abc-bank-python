from datetime import datetime
from date_provider import DateUtils


class Transaction:
    def __init__(self, amount, date=None):
        self.amount = amount
        if not date:
            self.transactionDate = datetime.now()
        else:
            if isinstance(date, str):
                self.transactionDate = DateUtils.toDate(date)
            else:
                self.transactionDate = date

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.amount == other.amount and DateUtils.toString(self.transactionDate) == DateUtils.toString(
                other.transactionDate)
        return False
