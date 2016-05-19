from nose.tools import assert_equal

from abcbank.account import Account, CHECKING

def test_accountBalance():
    testAccount = Account(CHECKING)
    testAccount.deposit(1000)
    assert_equal(testAccount.availableBalance, 1000, "Test available Balance")
    testAccount.withdraw(500)
    assert_equal(testAccount.availableBalance, 500, "Test available Balance after withdraw")
