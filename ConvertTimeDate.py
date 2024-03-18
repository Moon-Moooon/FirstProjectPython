import datetime


class ConvertTimeDate:
    _diviter = 1000

    @staticmethod
    def convert(line):
        line = line/ConvertTimeDate._diviter
        result = datetime.datetime.fromtimestamp(line)
        return result

