from datetime import datetime

from ZULU.constants import DIVIDER


class ConvertTimeDate:
    def convert(self, line):
        new_line = line/DIVIDER
        result = datetime.fromtimestamp(new_line)
        return result

    def get_сurrent_datetime(self):
        result = datetime.now().strftime('%Y-%m-%d-%H%M%S')
        return result
