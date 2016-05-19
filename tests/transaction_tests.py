from nose.tools import assert_is_instance, assert_equal
from abcbank.transaction import Transaction


def test_type():
    t = Transaction(5)
    assert_is_instance(t, Transaction, "correct type")


def test_TransactionEquality():
    T1 = Transaction(100, "01/01/2016")
    T2 = Transaction(100, "01/01/2016")
    assert_equal(T1, T2)
