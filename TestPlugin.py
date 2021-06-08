# -*- coding: utf-8 -*-
"""
Created on Sat May 22 20:21:48 2021

@author: sachi
""" 

import platform
#print(platform.python_version())

#C:\path\to\python_64bit.exe -m pip install pywinauto

import pywinauto, time 
from  pywinauto.application import Application 
from datetime import datetime


from pywinauto import application
from pywinauto import mouse 
 
 
 
def OpenLogFile():   
    #WritelogToFile("Starting to Log " )
    print("Starting to log")
    
def CloseLogFile():    
    #f.close()
    print("End of log")
def WritelogToFile(logtext):
    #f.write(str(logtext ))
    #f.write("\n")
    print(logtext)
    print("\n")
    
 
#f = open("QGISLogFile.txt", "a",encoding='utf-8')
OpenLogFile()
WritelogToFile("--------Will Open QGIS app--------")
app = Application(backend="uia").start("C:\\Program Files\\QGIS 3.16\\bin\\qgis-ltr-bin.exe", timeout=1)

WritelogToFile("--------Begin New Log--------")
WritelogToFile("1. Opened QGIS application")
app.set_focus
  

if app.window(title = "Untitled Project — QGIS").exists():
    print('yes')



main_dlg = app.window(title='Untitled Project — QGIS')
WritelogToFile("2. Got the main window dialog")
    
time.sleep(3)
#main_dlg.print_control_identifiers(filename='QGIS_controls.txt')
main_dlg.print_control_identifiers()


#dlgA = main_dlg.window(title="AequilibraE")
#dlgA.Button1.click()


'''
time.sleep(1)

#188,400 
pywinauto.mouse.click(button="left", coords=(57,393 ))
pywinauto.mouse.click(button="left", coords=(326,401  ))
WritelogToFile("3. Clicked on Aequilibrae->Project->Open Project")

  
 
proj_path = r'C:\Pradnya\AquilibraE_Project\sioux_falls_2020_02_15\1_project\SiouxFalls1.sqlite'

time.sleep(1)
proj_dlg = main_dlg.window(title='AequilibraE Project')
WritelogToFile("3. Got the Aequilibrae->Project->Open Project dialog")


#proj_dlg.print_control_identifiers()

proj_dlg.ComboBox1.Edit5.type_keys(proj_path)
WritelogToFile("4.Entered the project with full path to be opened")

proj_dlg.Open3.click()
WritelogToFile("5. Clicked on Aequilibrae->Project->Open Project->Open button")

time.sleep(5)


dlgerror= main_dlg.window(title_re ='.*error has.*', found_index =1)
WritelogToFile("6. Get the error message dialog")

WritelogToFile("7.*************Error MEssage*************")
WritelogToFile(dlgerror.window_text)

WritelogToFile("")
 
 
print(dlgerror.window_text)


 

dlgClose= main_dlg.window(title_re ='.*error has.*', found_index =0)
dlgClose.Button1.click()

WritelogToFile("8.Click on Close button of Error message window i.e Close the Error message window")
 


CloseLogFile()
'''


















'''
print('***************')
print(dlgerror.GroupBox1.child_window)
print('$$$$$$$$$$$$$$$')
print(dlgerror.GroupBox1.text)
'''
### ERror main_dlg.top_window.print_control_identifiers()
#dlgerror.top_window().print_control_identifiers()

#dlgerror.TitleBar1.Button1.click()
 
#dlgerror.MenuItem.dump_tree()
#dlgerror.Groupbox1.dump_tree()
#dlgerror.Scrollbar1.dump_tree()

 

#CHECK FOR ERROR WINDOW 
#'An error has occurred while executing Python code'
 
#main_dlg.print_control_identifiers(filename='Errortxt.txt')
#print(main_dlg.TitleBar1.print_control_identifiers() )
#print(main_dlg.TabItem3.Edit)
#print(main_dlg.TabItem3.Edit.text)



#print(main_dlg.TabItem2.window_text) #GENERAL
#print(main_dlg.TabItem1.window_text) # PLUGINS



#MenuItem = dlgA.PopupMenu.Items(i);



'''
main_dlg.Edit.type_keys("Hello pywinauto!\n\t It’s a sample text^A",
                        with_spaces=True,
                        with_newlines=True,
                        pause=0.5,
                        with_tabs=True)

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

#app = Application(backend="uia").connect(title='Untitled — Notepad')
#print(app.windows()) 
 
#app['Notepad'].menu_select("File->PageSetUp")

#app = Application(backend="uia").start('C:\\Program Files\\QGIS 3.16\\bin\\qgis-ltr-bin.exe', timeout=1)
#app.Connect(title="Untitled Project — QGIS", class_name='QgisApp')
#app = Application(backend="uia").start(r'C:\Program Files\QGIS 3.16\bin\qgis-ltr-bin.exe', timeout=5) # r = raw code 

#app = Application(backend="uia").connect(process=8916)
#app = Application().connect(path=r'C:\Program Files\QGIS 3.16\bin\qgis-ltr-bin.exe')
#app = Application().connect(title=".", class_name='QgisApp')
#print(app)

 #app = Application(backend="uia").connect(title=u"Untitled Project — QGIS", class_name='QgisApp')
#app = Application(backend="uia").connect(title_re=u".*roject*", class_name='QgisApp')

#app =Application()
#C:\ProgramData\Microsoft\Windows\Start Menu\Programs\QGIS 3.16

#app.start("C:\\Program Files\\QGIS 3.16\\bin\\qgis-ltr-bin.exe").Connect(title_re=".*ntitled.*")
 
#print(app.Untitled.print_control_identifiers())  
#, classname -QgisApp

#dlgA = app.Untitled.window(title="Qt5QWindowIcon")
#print(dlgA.windows())
#dlgA.Button1.click()
#app.Save.TypeKeys("test")

#dlgA = app.UntitledProject.window(title_re=".*qui*")
#dlgA.print_control_identifiers()

#app.UntitledProjectQGIS.print_control_identifiers()
#dlg = app.window(title="Untitled Project — QGIS")
#print(dlg.print_control_identifiers())

 


'''
print(app)
print(app.windows())
dlg = app.window(title="Untitled Project — QGIS")
print(dlg.print_control_identifiers())#child_window(title="Untitled Project — QGIS", class_name="Qt5QWindowIcon")
'''
