# Given CSV file -> Group of people
# perform matching - apart from themselves
# send the email - Parse the CSV - for name vs email

# Extract data from CSV - JSON parser -> Can't select itself can select users that are already selected
# Need to map each user to a given receiver 
# can't assign user to itself or user that is already taken


import csv
from collections import deque
import random
import copy

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.receive = None
        self.give = None

    def getReceive(self):
        return self.receive
    
    def getGive(self):
        return self.give

class UserRepo:
    def __init__(self):
        self.fileDir = "./Repo/group1.csv"
        self.fileData = deque()

    def parseCsv(self):
        
        
        with open(self.fileDir, mode="r", encoding='utf-8') as file:
            csvFile = csv.DictReader(file)

            for line in csvFile:
                self.fileData.append(User(line["Name"], line["Email"]))

        return self.fileData

class SecretSanta:
    def __init__(self, users):
        self.adjacenyList = {}
        self.users = users

    def santaMap(self):

        arr = copy.deepcopy(self.users)
        
        for i in range(len(arr)-1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]

        
        for i in range(len(arr)):
            if i == (len(arr)-1):
                self.adjacenyList[arr[i].email] = arr[0].email
            else:
                self.adjacenyList[arr[i].email] = arr[i+1].email


        return self.adjacenyList

if __name__ == "__main__":
    userData = UserRepo().parseCsv()
    mapData = SecretSanta(userData).santaMap()
    print(mapData)