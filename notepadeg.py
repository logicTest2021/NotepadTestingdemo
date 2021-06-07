# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:32:06 2021

@author: sachi
"""



import platform
#print(platform.python_version())

#C:\path\to\python_64bit.exe -m pip install pywinauto

 	 
import pywinauto, time 
from  pywinauto.application import Application 



from pywinauto import application


# Import pywinauto Application class
#from pywinauto.application import Application




#https://pywinauto.readthedocs.io/en/latest/HowTo.html#how-to-specify-a-usable-application-instance
#app = Application(backend="uia").start('C:\\Program Files\\QGIS 3.16\\bin\\qgis-ltr-bin.exe', timeout=1)
app = Application(backend="uia").start('Notepad.exe', timeout=1)
if app.window(title = "Untitled — Notepad").exists():
    print('yes')
    
main_dlg = app.window(title='Untitled - Notepad')
print("Opened a notepad")

#main_dlg.print_control_identifiers()

main_dlg.Edit.type_keys("Hello pywinauto!\n\t It’s a sample text^A",
                        with_spaces=True,
                        with_newlines=True,
                        pause=0.1,
                        with_tabs=True)
'''
font_menu = main_dlg.menu_select('Format->Font...')
font_dlg = app.Font
font_type = font_dlg.ComboBox
font_type.select('Comic Sans MS')
font_style = font_dlg.ComboBox2
font_style.select('Bold')
font_size = font_dlg.ComboBox3
font_size.type_keys('18')
font_dlg.OK.click()
'''
print("Done!. Written on notepad")