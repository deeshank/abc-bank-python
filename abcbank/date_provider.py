import datetime


class DateUtils:
    @staticmethod
    def now():
        """

        :return: Current date time
        """
        return datetime.datetime.now()

    @staticmethod
    def add(date, days):
        """
        Add x days to the date

        :param date: date in string format
        :param days: number of days to be added
        :return: date in string format
        """
        return (DateUtils.toDate(date) + datetime.timedelta(days=days)).strftime("%m/%d/%Y")

    @staticmethod
    def toDate(date_str):
        """
        Convert the date in string format to datetime format

        :param date_str: date in string format
        :return: date in datetime format
        """
        if isinstance(date_str,str):
            return datetime.datetime.strptime(date_str, '%m/%d/%Y')
        else:
            return date_str

    @staticmethod
    def find_no_days(date1_str, date2_str):
        """
        Find no of days between 2 dates

        :param date1_str: date1 in string format
        :param date2_str: date2 in string format
        :return: no of day between 2 dates
        """
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
        """
        Return datetime object in string format

        :param date: datetime object
        :return: datetime in string
        """
        return date.strftime("%m/%d/%Y")

    @staticmethod
    def isDateWithinRange(date, startDate, endDate):
        """
        Checks if the given date is within the time frame

        :param date:
        :param startDate:
        :param endDate:
        :return: boolean true/false
        """
        if isinstance(date, str):
            date = DateUtils.toDate(date)
        if isinstance(startDate, str):
            startDate = DateUtils.toDate(startDate)
        if isinstance(endDate, str):
            endDate = DateUtils.toDate(endDate)
        return DateUtils.find_no_days(date, startDate) <= 0 <= DateUtils.find_no_days(date, endDate)
