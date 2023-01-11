import csv
import sys


class FileReader:
    def __init__(self, path: str):
        self.path = path
        self.extension = self.set_extension(path)

    @staticmethod
    def set_extension(path: str):
        if path.endswith('.csv'):
            return 'csv'
        elif path.endswith('.txt'):
            return 'txt'
        else:
            raise Exception("Sorry, Choose .txt, .csv or extension")

    # Current example: {'id_seller': '0', 'id_item': '0', 'count': '5', 'price': '10', 'discount': '[1,2],[3,4],[2]', 'delivery': '[x+2, 1],[x+1, 2],[x+4]'}
    def get_record_by_id_column(self, id_column_name: str, id_column_value: int):
        with open(self.path, 'r') as file:
            if self.extension == 'csv':
                csv_reader = csv.DictReader(file, delimiter=';')
                for line in csv_reader:
                    if line[id_column_name] == str(id_column_value):
                        return line

    def get_file_records(self):
        with open(self.path, 'r') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            for line in csv_reader:
                yield line
