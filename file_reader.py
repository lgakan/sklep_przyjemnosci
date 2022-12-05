import csv
import sys


class FileReader:
    def __init__(self, path: str):
        self.path = self.set_path(path)
        self.extension = self.set_extension(path)
        # self.file_content = []

    @staticmethod
    def set_path(path: str):
        try:
            open(path, 'r')
        except OSError as e:
            print(f"Unable to open {path}: {e}", file=sys.stderr)
        return path

    @staticmethod
    def set_extension(path: str):
        if path.endswith('.csv'):
            return 'csv'
        elif path.endswith('.txt'):
            return 'txt'
        else:
            raise Exception("Sorry, Choose .txt, .csv or extension")

    def get_column_from_file(self, column_name: str):
        with open(self.path, 'r') as file:
            column_content = []
            if self.extension == 'csv':
                csv_reader = csv.DictReader(file, delimiter=';')
                for line in csv_reader:
                    if column_name == 'discount' or column_name == 'delivery':
                        # discount/delivery list without last element (np.["[x+2,1", "[x+1,2"] and last_el = [x+4]or[1]
                        strings_list, last_el = line[column_name].split('],')[:-1], line[column_name].split('],')[-1]
                        # Getting [['x+2', 1], ['x+1', 2]]
                        for i in range(len(strings_list)):
                            strings_list[i] = strings_list[i][1:].split(',')
                            strings_list[i][1] = int(strings_list[0][1])
                        # Adding last_el
                        if column_name == 'discount':
                            strings_list.append([int(last_el[1:-1])])
                        elif column_name == 'delivery':
                            strings_list.append([last_el[1:-1]])
                        column_content.append(strings_list)
                    else:
                        column_content.append(line[column_name])
                return column_content
            elif self.extension == 'txt':
                # TODO: Implement me :(
                pass

    # Current example: {'id_seller': '0', 'id_item': '0', 'count': '5', 'price': '10', 'discount': '[1,2],[3,4],[2]', 'delivery': '[x+2, 1],[x+1, 2],[x+4]'}
    # TODO: Possibility to upgrade (for example: use it for sellers file (multi_records would be returned)
    def get_record_by_id_column(self, id_column_name: str, id_column_value: int):
        with open(self.path, 'r') as file:
            if self.extension == 'csv':
                csv_reader = csv.DictReader(file, delimiter=';')
                for line in csv_reader:
                    if line[id_column_name] == str(id_column_value):
                        return line