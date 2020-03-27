import sys
import os
from github import Github

path = "" add the path of the folder

username = "" #Insert your github username here
password = "" #Insert your github password here

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()