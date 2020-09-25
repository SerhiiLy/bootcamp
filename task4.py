# Create micro library that allows users to work with notes about books
# authors. Note should contain author_name, note, rating
# (rating - is 0 - 1 rating of the author)
#
# Micro lib should contain the next functionality:
#    1) Read notes from file
#    2) Add notes to file
#    3) Print notes to console
#    4) Get author with the highest rating
#    5) Get author with the lowest rating
#    6) Get average rating among all authors
# class

import csv


class Note:
    def __init__(self, path='sw_data.csv'):
        self.path = path

    # Read notes from file
    def read_notes(self):
        try:
            with open(self.path) as file:
                reader = csv.reader(file)
                return list(reader)
        except FileNotFoundError:
            print("Something went wrong when writing to the file")

    # Add notes to file
    def add_notes(self, author_name, note, rating):
        try:
            data = [[author_name, note, rating]]
            with open(self.path, "a") as file:
                writer = csv.writer(file)
                for row in data:
                    writer.writerow(row)
        except:
            print("Something went wrong when writing to the file")

    # Overloading str for use print notes in console
    def __str__(self):
        arr = ''
        for author_name, note, rating in self.read_notes():
            arr += '{0:15} {1:50} {2:4}\n'.format(author_name, note, rating)
        return arr

    # Get author with the highest rating
    def get_author_with_highest_rating(self):
        data = self.read_notes()
        max = 0
        i = 0
        for _, _, rating in data:
            if rating.isdigit() or rating.replace('.', '', 1).isdigit():
                k = float(rating)
                if max <= k:
                    max = k
                    index = i
            i += 1
        return data[index][0]

    # Get author with the lowest rating
    def get_author_with_lowest_rating(self):
        data = self.read_notes()
        min = 0
        i = 0
        for _, _, rating in data:
            if rating.isdigit() or rating.replace('.', '', 1).isdigit():
                k = float(rating)
                if min >= k:
                    min = k
                    index = i
            i += 1
        return data[index][0]

    # Get average rating among all authors
    def get_average_rating(self):
        count = 0
        sum = 0
        for _, _, rating in self.read_notes():
            if rating.isdigit() or rating.replace('.', '', 1).isdigit():
                sum += float(rating)
                count += 1
        average = sum / count
        return average
