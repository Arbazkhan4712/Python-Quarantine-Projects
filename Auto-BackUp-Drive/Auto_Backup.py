import os
import re 
import psutil
import shutil
from time import sleep

def usb():
    drps = psutil.disk_partitions()
    drives = [dp.device for dp in drps if dp.fstype == 'FAT32']
    d = str(drives)
    res1 = "".join(re.split("[^a-zA-Z]*", d))
    # os.chdir(res1+":/Backup")
    finaldist = (res1+":/Backup")
    # print(os.listdir())
    return finaldist

def check(): 
    drps = psutil.disk_partitions()
    drives = [dp.device for dp in drps if dp.fstype == 'FAT32']
    d = str(drives)
    res1 = "".join(re.split("[^a-zA-Z]*", d))
    # os.chdir(res1+":/Backup")
    # print(os.listdir())
    if res1.isalpha():
        print("USB Connect")
        return 1
    else:
        print("No USB")
        return 0
    

if check() == 1:
    source = ("C:\\Users\\arbaz\\Desktop\\Open-cv\\test")
    os.chdir(source)
    files = os.listdir()
    print(files)
    path = usb()
    print(path)

    for file in files:
        try:
            if os.listdir() != os.listdir(path):
                shutil.copy(file,path)
                print(file+ " Creating Backup")
            else:
                print(file +" present")  
        except:
            print("Error")

else:
    print("No USB Connected!")



    
