import os
import csv


class FileReader:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def read_files(self):
        data = []
        for filename in os.listdir(self.folder_path):
            with open(os.path.join(self.folder_path, filename), 'r') as file:
                file_iter = iter(file)
                name = next(file_iter).strip()
                weight = next(file_iter).strip()
                description = next(file_iter).strip()
                data.append({'name': name, 'weight': weight, 'description': description})
        return data


file_reader = FileReader("descriptions")
data = file_reader.read_files()

with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'weight', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in data:
        writer.writerow(item)
