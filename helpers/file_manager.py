import csv

FILE_PATH = './data/ut_scrapper.csv'

class FileManager():
    def __init__(self) -> None:
        self.field_names = ['title', 'date', 'link']

    def check_file(self):
        try:
            v_file = csv.DictReader(open(FILE_PATH, 'r'))
            print("The file ut_scrapper.csv already exists. Moving on...")
        except:
            self.create_file()
            print("The file ut_scrapper.csv was not found. Created a new one...")

    def create_file(self):
        with open(FILE_PATH, 'w', newline='') as csv_file:
            c_writer = csv.DictWriter(csv_file, fieldnames=self.field_names)
            c_writer.writeheader()

    def write_file(self, title, date, link):
        try:
            with open(FILE_PATH, 'a', newline='') as csv_file:
                c_writer = csv.DictWriter(csv_file, fieldnames=self.field_names)

                c_writer.writerow({'title': title, 'date': date, 'link': link})

                csv_file.close()
        except:
            print("Something went wrong :(")