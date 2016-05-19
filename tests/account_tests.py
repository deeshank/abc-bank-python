from nose.tools import assert_equal

from abcbank.account import Account, CHECKING



def test_accountBalance():
    testAccount = Account(CHECKING)
    testAccount.deposit(1000)
    assert_equal(testAccount.availableBalance, 1000, "Test available Balance")
    testAccount.withdraw(500)
    assert_equal(testAccount.availableBalance, 500, "Test available Balance after withdraw")


def test_checkDateFormat():
    assert_equal(Account(CHECKING).getTransaction("01-01-2016", "01-01-2016").message, "Incorrect date format")


def test_checkNoOfTransaction():
    test_acc = Account(CHECKING)
    test_acc.deposit(500, "01/01/2016")
    test_acc.deposit(500, "01/02/2016")
    test_acc.deposit(500, "01/03/2016")
    test_acc.deposit(500, "01/04/2016")
    test_acc.deposit(500, "01/05/2016")
    test_acc.deposit(500, "01/06/2016")
    test_acc.deposit(500, "01/07/2016")
    assert_equal(len(test_acc.getTransaction("01/02/2016", "01/04/2016")), 3)
