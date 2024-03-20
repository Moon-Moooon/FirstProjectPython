import csv

from ZULU.constants import COLUMNS_NAME
from ZULU.constants import FILE_NAME


class SaveInfo:
    @staticmethod
    def write(a):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(COLUMNS_NAME)
            writer = csv.DictWriter(file, fieldnames=COLUMNS_NAME)
            writer.writerows(a)

