import csv

from constants import COLUMNS_NAME
from constants import FALE_NAME


class SaveInfo:
    @staticmethod
    def write(a):
        with open(FALE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(COLUMNS_NAME)
            writer = csv.DictWriter(file, fieldnames=COLUMNS_NAME)
            writer.writerows(a)

