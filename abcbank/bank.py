class Bank:
    def __init__(self):
        self.customers = []

    def addCustomer(self, customer):
        """
        Add a customer to the bank

        :param customer: Customer Name
        :return: None
        """
        self.customers.append(customer)

    def customerSummary(self):
        summary = "Customer Summary"
        for customer in self.customers:
            summary = summary + "\n - " + customer.name + " (" + self._format(customer.numAccs(), "account") + ")"
        return summary

    def _format(self, number, word):
        return str(number) + " " + (word if (number == 1) else word + "s")

    def totalInterestPaid(self):
        """
        Total Interest Paid for all customer for all acounts the customer possess

        :return: interest payout
        """
        total = 0
        for c in self.customers:
            total += c.totalInterestEarned()
        return total

    def getFirstCustomer(self):
        try:
            self.customers = None
            return self.customers[0].name
        except Exception as e:
            print(e)
            return "Error"
