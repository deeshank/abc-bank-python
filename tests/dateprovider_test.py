from nose.tools import assert_equals

from abcbank.date_provider import DateUtils


def test_findnodays():
    date1 = "01/01/2016"
    date2 = "01/01/2017"
    assert_equals(DateUtils.find_no_days(date1, date2), 366)


def test_add_date():
    date1 = "01/01/2016"
    assert_equals(DateUtils.add(date1, 5), "01/06/2016")


def test_isdateWithinRange():
    date = "01/04/2016"
    startDate = "01/01/2016"
    endDate = "01/06/2016"
    assert_equals(DateUtils.isDateWithinRange(date, startDate, endDate), True)

    date = "01/04/2015"
    startDate = "01/01/2016"
    endDate = "01/06/2016"
    assert_equals(DateUtils.isDateWithinRange(date, startDate, endDate), False)

    date = "01/04/2017"
    startDate = "01/01/2016"
    endDate = "01/06/2016"
    assert_equals(DateUtils.isDateWithinRange(date, startDate, endDate), False)

    date = "01/01/2016"
    startDate = "01/01/2016"
    endDate = "01/06/2016"
    assert_equals(DateUtils.isDateWithinRange(date, startDate, endDate), True)

    date = "01/06/2016"
    startDate = "01/01/2016"
    endDate = "01/06/2016"
    assert_equals(DateUtils.isDateWithinRange(date, startDate, endDate), True)
