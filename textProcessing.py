# Text Processing Program by Ryan Banafshay
#
# This program takes a data file and processes the text into a more
# readable format. If data is inputted incorrectly in the data file,
# the program will ask the user to input it again correctly. The data
# is then converted into a pickle file and then displayed back to the user
#

import csv
import pickle
import re

# defining the person class with identifying parameters
class Person:

    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    def display(self):
        print("Employee id: ", self.id)
        print(self.last, " ", self.mi, " ", self.first)
        print(self.phone, "\n")

def processInput():
    employees = dict()      # defining a dictionary to hold people objects of the employees
    with open("data/data.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)     # skip first line of the data file
        for row in csvreader:
            row[0] = row[0].title()     # convert last name to title case
            row[1] = row[1].title()     # convert first name to title case
            if row[2] == "":
                row[2] = "X"
            else:
                row[2] = row[2].upper()

            # check to see if ID is in proper format via regex
            # if not then ask user to re-enter properly
            checkName = row[3]
            idMatched = re.match("[a-zA-Z][a-zA-Z][0-9][0-9][0-9][0-9]", checkName)
            isID_match = bool(idMatched)
            if not isID_match:
                print("ID invalid: ", checkName)
                print("ID is two letters followed by 4 digits")
                checkName = input("Please enter a valid id: ")

            # check to see if the phone number is in proper format via regex
            # if not then ask user to re-enter properly
            phoneNum = row[4]
            matched = re.match("[0-9][0-9][0-9][-][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]", phoneNum)
            is_match = bool(matched)
            if not is_match:
                print("Phone ", phoneNum, " is invalid")
                print("Enter phone number in form 123-456-7890")
                phoneNum = input("Enter phone number: ")

            # create a person object using their last name + first name as a variable name
            key = row[3]
            name = row[0] + row[1]
            name = Person(row[0], row[1], row[2], checkName, phoneNum)
            employees[key] = name       # add the employee object to the dictionary with the ID as a key
        return employees


def main():
    employees = processInput()
    pickledObject = pickle.dumps(employees)
    unpickledObject = pickle.loads(pickledObject)

    # display all employee information in the dictionary
    print("\n\n\nEmployee list:\n\n")
    for key in employees:
        unpickledObject[key].display()


if __name__ == "__main__":
    main()


