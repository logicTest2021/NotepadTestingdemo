import platform
import pywinauto, time 
from  pywinauto.application import Application 
from pywinauto import application
import os

print("Hi There ")
print("Lets use pywinauto")

print(platform.python_version())


os.system("C:\\Windows\\notepad.exe")
print("opened notepad")

'''
app = Application(backend="uia").start('C:\\Program Files\\QGIS 3.16\\bin\\qgis-ltr-bin.exe', timeout=1)
app.print_control_identifiers()
print("Opened QGIS exe")
'''
