print("Hi There ")
print("Lets use pywinauto")


from pywinauto import application
app = Application(backend="uia").start('C:\\Program Files\\QGIS 3.16\\bin\\qgis-ltr-bin.exe', timeout=1)
app.print_control_identifiers()
print("Opened QGIS exe")
