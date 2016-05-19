import datetime


class DateUtils:
    @staticmethod
    def now():
        return datetime.datetime.now()

    @staticmethod
    def add(date, days):
        return (DateUtils.toDate(date) + datetime.timedelta(days=days)).strftime("%m/%d/%Y")

    @staticmethod
    def toDate(date_str):
        if isinstance(date_str,str):
            return datetime.datetime.strptime(date_str, '%m/%d/%Y')
        else:
            return date_str

    @staticmethod
    def find_no_days(date1_str, date2_str):
        if isinstance(date1_str, str):
            date1 = DateUtils.toDate(date1_str)
        else:
            date1 = date1_str
        if isinstance(date2_str, str):
            date2 = DateUtils.toDate(date2_str)
        else:
            date2 = date2_str
        return (date2 - date1).days

    @staticmethod
    def toString(date):
        return date.strftime("%m/%d/%Y")

    @staticmethod
    def isDateWithinRange(date, startDate, endDate):
        if isinstance(date, str):
            date = DateUtils.toDate(date)
        if isinstance(startDate, str):
            startDate = DateUtils.toDate(startDate)
        if isinstance(endDate, str):
            endDate = DateUtils.toDate(endDate)
        return DateUtils.find_no_days(date, startDate) <= 0 <= DateUtils.find_no_days(date, endDate)
