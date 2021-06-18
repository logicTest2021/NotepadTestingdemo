# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:19:08 2021

@author: sachi
"""
 
import pywinauto,time
from  pywinauto.application import Application 
 
    
def CloseLogFile():    
    f.close()

def WritelogToFile(logtext):
    #f.write(str(logtext ))
    #f.write("\n")
    print(logtext)
    print("\n")
    
    
def OpenQGISApp():
    WritelogToFile("----------------Starting to Log----------------------------") 
    app = Application(backend="uia").start('C:\\Program Files\\QGIS 3.16\\bin\\qgis-ltr-bin.exe', timeout=10)
    WritelogToFile("1. Opened QGIS application")
    return app

def MouseclicksonMenus(arg1, arg2):
    pywinauto.mouse.click(button="left", coords=(arg1,arg2 ))
    
def OpenProject(main_dlg):    
    WritelogToFile("Now click on Aequilibrae menus ")
   
    MouseclicksonMenus(57,393)
    MouseclicksonMenus(326,401)    
    WritelogToFile("3. Clicked on Aequilibrae->Project->Open Project")        
    #time.sleep(1)
    
    proj_dlg = main_dlg.window(title='AequilibraE Project')
    WritelogToFile("After click on open project ")
    #print(proj_dlg.print_control_identifiers())
    
     
    proj_path = r'C:\Pradnya\AquilibraE_Project\sioux_falls_2020_02_15\1_project\SiouxFalls1.sqlite'
    proj_dlg.ComboBox1.Edit45.type_keys(proj_path)
    WritelogToFile("4.Entered the project with full path to be opened")
    proj_dlg.Button15.click()
    WritelogToFile("Opened file with wrong spelling -SiouxFalls1-sqlite")
    
    
    
    dlgerror= main_dlg.window(title_re ='.*error has.*', found_index =1)   
    #print(dlgerror.window_text)
    WritelogToFile("6. Got the error message dialog")
    WritelogToFile("7.*************Error MEssage*************")
    WritelogToFile(str(dlgerror.window_text))
    WritelogToFile("")
    main_dlg.window(title_re ='.*error has.*', found_index =0).Button1.click()
        
def DisplayAequilibraEPanel(main_dlg,app):  
    MouseclicksonMenus(214,76)
    WritelogToFile('Clicked on View')
    time.sleep(3)
    pywinauto.mouse.scroll(coords=(614, 1552))
    time.sleep(2)    
    pywinauto.mouse.move(coords=(624, 1554))
    WritelogToFile('Moved to Panels')
    #MouseclicksonMenus(614,552)
    time.sleep(2)
    pywinauto.mouse.scroll(coords=(1248, 1313))
    pywinauto.mouse.move(coords=(1258, 1319))
    MouseclicksonMenus(1258,1319)
    WritelogToFile('Clicked on AequilibraE')
    #MouseclicksonMenus(1258,1319)
    #MouseclicksonMenus(1248,1313) #Menuitem AEquilibraE
    time.sleep(2)    
     
   
 
def OpenProjectOSM(app):    
    WritelogToFile("-------Testing of Project->Open Project From OSM")
    
    MouseclicksonMenus(57,393)
    MouseclicksonMenus(300,438)
    WritelogToFile("Clicked on Project->OSM menus") 
    
    proj_dlg1 = app.window(title='AequilibraE')
    #proj_dlg1 = app.window(title='AequilibraE').wait('ready',timeout=5)
    WritelogToFile("3. Got the Aequilibrae->Project->Project-Create Project From OSM")
    WritelogToFile(proj_dlg1.print_control_identifiers())
    time.sleep(4)
   
    
    proj_dlg1.placename.click()    
    WritelogToFile("Clicked on Placename") 
    time.sleep(2)
    #proj_dlg1.print_control_identifiers()    
    proj_dlg1.Edit1.type_keys("BLUE RIDGE, GA") 
    WritelogToFile("Entered BlueRidge as placename") 
    time.sleep(2)
    
    proj_dlg1.Button2.click()    
    WritelogToFile("Clicked on Choose File Output Button") 
    time.sleep(2)
    
    proj_dlg1.ComboBox1.Edit5.type_keys("BlueRidge")
    WritelogToFile("Entered File Name with sqlite extension") 
    time.sleep(2)
    #proj_dlg1.window("Open").print_control_identifiers()
    proj_dlg1.Open4.click()
    time.sleep(1)
    proj_dlg1.Button3.click()    
    
    time.sleep(30)
    
    WritelogToFile("------------30 sec over--------------")
    proj_dlgclose = app.window(title_re=".*Procedure*")
    WritelogToFile("The procedure window is displayed") 
    
    #proj_dlgclose.print_control_identifiers()
    WritelogToFile()(proj_dlgclose.Edit0.window_text())
    proj_dlgclose.Button1.click()
        
    
    
    
    
     
    
    
WritelogToFile("1. Opened QGIS application")
 

app =OpenQGISApp() 
dlg = app.top_window()
#print(dlg.print_control_identifiers()

#app.set_focus

main_dlg = app.top_window() 
#print(main_dlg.print_control_identifiers())

#OpenProject(main_dlg)
#DisplayAequilibraEPanel(main_dlg,app)
#OpenProjectOSM(app)
DisplayAequilibraEPanel(main_dlg, app)






'''
------------------------------------------------------
print("Now click on Aequilibrae menus ")
MouseclicksonMenus(57,393)
MouseclicksonMenus(326,401)

WritelogToFile("3. Clicked on Aequilibrae->Project->Open Project")
 

#time.sleep(1)
proj_dlg = main_dlg.window(title='AequilibraE Project')
#WritelogToFile("3. Got the Aequilibrae->Project->Open Project dialog")
WritelogToFile("After click on open project ")
#print(proj_dlg.print_control_identifiers())

 
proj_path = r'C:\Pradnya\AquilibraE_Project\sioux_falls_2020_02_15\1_project\SiouxFalls1.sqlite'
proj_dlg.ComboBox1.Edit45.type_keys(proj_path)
WritelogToFile("4.Entered the project with full path to be opened")
proj_dlg.Button15.click()
WritelogToFile("Opened file with wrong spelling -SiouxFalls1-sqlite")



dlgerror= main_dlg.window(title_re ='.*error has.*', found_index =1)
#dlgerror.Button1.click() 
#print(dlgerror.window_text)
WritelogToFile("6. Got the error message dialog")
WritelogToFile("7.*************Error MEssage*************")
WritelogToFile(str(dlgerror.window_text))
WritelogToFile("")
main_dlg.window(title_re ='.*error has.*', found_index =0).Button1.click()





------------------------------------------------------
'''
#proj_dlg.print_control_identifiers(filename="projdlg.txt")

#proj_path = r'C:\Pradnya\AquilibraE_Project\sioux_falls_2020_02_15\1_project\SiouxFalls1.sqlite'
#proj_path = 'C:\\Pradnya\\AquilibraE_Project\\sioux_falls_2020_02_15\\1_project\\SiouxFalls1.sqlite'

'''
#proj_dlg.ComboBox1.Edit5.type_keys(proj_path)
proj_dlg.ComboBox1.Edit5.type_keys(proj_path)
#WritelogToFile("4.Entered the project with full path to be opened")

proj_dlg.Open3.click()
WritelogToFile("5. Clicked on Aequilibrae->Project->Open Project->Open button")

#time.sleep(5)


dlgerror= main_dlg.window(title_re ='.*error has.*', found_index =1)
WritelogToFile("6. Get the error message dialog")

WritelogToFile("7.*************Error MEssage*************")
WritelogToFile(dlgerror.window_text)

WritelogToFile("")
'''

#proj_dlg.print_control_identifiers(filename="projdlg.txt")

#proj_path = r'C:\Pradnya\AquilibraE_Project\sioux_falls_2020_02_15\1_project\SiouxFalls1.sqlite'
#proj_path = 'C:\\Pradnya\\AquilibraE_Project\\sioux_falls_2020_02_15\\1_project\\SiouxFalls1.sqlite'

'''
#proj_dlg.ComboBox1.Edit5.type_keys(proj_path)
proj_dlg.ComboBox1.Edit5.type_keys(proj_path)
#WritelogToFile("4.Entered the project with full path to be opened")

proj_dlg.Open3.click()
WritelogToFile("5. Clicked on Aequilibrae->Project->Open Project->Open button")

#time.sleep(5)


dlgerror= main_dlg.window(title_re ='.*error has.*', found_index =1)
WritelogToFile("6. Get the error message dialog")

WritelogToFile("7.*************Error MEssage*************")
WritelogToFile(dlgerror.window_text)

WritelogToFile("")



 
#dlg = app.top_window()
#print(dlg.print_control_identifiers())
#app.set_focus

#main_dlg = app.top_window() 
#print(main_dlg.print_control_identifiers())




#proj_dlg.print_control_identifiers(filename="projdlg.txt")
#proj_path = r'C:\Pradnya\AquilibraE_Project\sioux_falls_2020_02_15\1_project\SiouxFalls1.sqlite'
#proj_path = 'C:\\Pradnya\\AquilibraE_Project\\sioux_falls_2020_02_15\\1_project\\SiouxFalls1.sqlite'

#proj_dlg.ComboBox1.Edit5.type_keys(proj_path)
proj_dlg.ComboBox1.Edit5.type_keys(proj_path)
#WritelogToFile("4.Entered the project with full path to be opened")

proj_dlg.Open3.click()
WritelogToFile("5. Clicked on Aequilibrae->Project->Open Project->Open button")

#time.sleep(5)


dlgerror= main_dlg.window(title_re ='.*error has.*', found_index =1)
WritelogToFile("6. Get the error message dialog")

WritelogToFile("7.*************Error MEssage*************")
WritelogToFile(dlgerror.window_text)

WritelogToFile("")
'''
