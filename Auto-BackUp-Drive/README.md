# Auto-BackUp-Drive
It will automatically backup your data into a USB drive using python.
It can also detect if a USB Drive is Connected or Not.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                  [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)          [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

# Dependencies:

*pyinstaller*
```
pip install pyinstaller
```

# ADD PATH Source Folder:
```
source = ("")#ADD THE PATH OF The Source Folder

finaldist = (res1+":/Backup")#Create a Folder nmae with Backup
```

# Run:
Convert the python file into .exe 
```
pyinstaller Auto_Backup.py --onefile
```

# Auto Start-Up Setup:

*1. Add The Drive letter in backup.bat*

*2. Run backup.bat*

*3.It will automatically run the backup script*

# Note:

*1. Connect only One USB To Run the Backup without Errors*

*2. The USB should be of FAT32 Type*

## License & Copyright
© [Arbaz Khan](https://arbazkhan4712.github.io/Contact.html)

Licensed under the [MIT License](LICENSE)
