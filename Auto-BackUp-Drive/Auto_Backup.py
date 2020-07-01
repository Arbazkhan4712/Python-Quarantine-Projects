import subprocess
from time import sleep
import shutil
import os

def storage_mount_check(n):
    mnt_stg='wmic logicaldisk where drivetype=2 get deviceid, volumename, description'           # Removable Disk
    lcl_stg='wmic logicaldisk where drivetype=3 get deviceid, volumename, description'           # Local Disk
    nt_stg='wmic logicaldisk where drivetype=4 get deviceid, volumename, description'            # Network Drive
    cd_stg='wmic logicaldisk where drivetype=5 get deviceid, volumename, description'            # CD ROM

    if n==1:
        mnt_dev_op=str(subprocess.check_output(mnt_stg),'utf-8')
    elif n==2:
        mnt_dev_op=str(subprocess.check_output(lcl_stg),'utf-8')
    elif n==3:
        mnt_dev_op=str(subprocess.check_output(nt_stg),'utf-8')
    elif n==4:
        mnt_dev_op=str(subprocess.check_output(cd_stg),'utf-8')
    else:
        mnt_dev_op='Invalid Input'

    return mnt_dev_op

def backup(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def usr_ip():
    n=int(input('Backup Mounter \n1.To View Mounted Devices \n2.Backup \n3.Exit \nChoose the above options to proceed: '))
    if n==1:
        ip=int(input('Device Mount Checker: \n1.Pendrive and SD Card \n2.Local Disk \n3.Network Mount \n4.CD-ROM \nCheck for available mounts: '))
        print(storage_mount_check(ip))
    elif n==2:
        mnt1=input('To Backup pls enter the FROM drive id with colon: ')
        mnt2=input('To Backup pls enter the TO drive id with colon: ')
        print(backup(str(mnt1),str(mnt2)))
    else:
        sleep(2)
        print('Have a nice day')
    

usr_ip()