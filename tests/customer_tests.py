from nose.tools import assert_equals, nottest

from abcbank.account import Account, CHECKING, SAVINGS, MAXI_SAVINGS
from abcbank.customer import Customer


def test_statement():
    checkingAccount = Account(CHECKING)
    savingsAccount = Account(SAVINGS)
    henry = Customer("Henry").openAccount(checkingAccount).openAccount(savingsAccount)
    checkingAccount.deposit(100.0)
    savingsAccount.deposit(4000.0)
    savingsAccount.withdraw(200.0)
    assert_equals(henry.getStatement(),
                  "Statement for Henry" +
                  "\n\nChecking Account\n  deposit $100.00\nTotal $100.00" +
                  "\n\nSavings Account\n  deposit $4000.00\n  withdrawal $200.00\nTotal $3800.00" +
                  "\n\nTotal In All Accounts $3900.00")


def test_oneAccount():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    assert_equals(oscar.numAccs(), 1)


def test_twoAccounts():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    oscar.openAccount(Account(CHECKING))
    assert_equals(oscar.numAccs(), 2)


def test_transfer():
    bob = Customer("Bob").openAccount(CHECKING)
    bob.openAccount(SAVINGS)
    bob.accounts[CHECKING].deposit(500)

    status = bob.transfer(CHECKING, SAVINGS, 100)
    assert_equals(status, "Transfer Succeeded", "Checking status of transfer")
    assert_equals(bob.accounts[CHECKING].availableBalance, 400, "Checking balance after transfer")
    assert_equals(bob.accounts[SAVINGS].availableBalance, 100, "Checking balance after transfer")

    bob.accounts[SAVINGS].deposit(400)
    assert_equals(bob.accounts[SAVINGS].availableBalance, 500, "Checking balance after deposit")

    status = bob.transfer(MAXI_SAVINGS, CHECKING, 100)
    assert_equals(status, "Invalid Account")


@nottest
def test_threeAccounts():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    oscar.openAccount(Account(CHECKING))
    assert_equals(oscar.numAccs(), 3)
