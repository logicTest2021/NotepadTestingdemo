import platform
import pywinauto, time 
from  pywinauto.application import Application 
from pywinauto import application
import os


import sys
from .base_application import WindowSpecification  # noqa: W0611

if sys.platform == 'win32':
    from .windows.application import Application  # noqa: W0611
else:
    from .linux.application import Application  # noqa: W0611

__all__ = ["WindowSpecification", "Application"]


print("Hi There ")
print("Lets use pywinauto")

print(platform.python_version())

'''
os.system("C:\\Windows\\notepad.exe")
print("opened notepad")
'''



app = Application(backend="uia").start('C:\\Windows\\system32\\Notepad.exe', timeout=1)    
main_dlg = app.window(title='Untitled - Notepad')
print("Opened a notepad")

#main_dlg.print_control_identifiers()

main_dlg.Edit.type_keys("Hello pywinauto!\n\t It’s a sample text^A",
                        with_spaces=True,
                        with_newlines=True,
                        pause=0.1,
                        with_tabs=True)

print('done!')


'''
app = Application(backend="uia").start('C:\\Program Files\\QGIS 3.16\\bin\\qgis-ltr-bin.exe', timeout=1)
app.print_control_identifiers()
print("Opened QGIS exe")
'''
