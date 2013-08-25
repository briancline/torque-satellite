from os.path import exists
from base import BackendEngine
import csv


class CSVBackend(BackendEngine):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_request(self, request):
        needs_headers = (not exists(self.file_name))

        with open(self.file_name, 'a') as csv_file:
            writer = csv.writer(csv_file)
            if needs_headers:
                writer.writerow(request.keys())

            writer.writerow(request.values())

        return True

    def read_request(self, request):
        raise NotImplemented
