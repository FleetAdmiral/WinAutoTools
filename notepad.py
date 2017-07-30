from pywinauto.application import Application
# Run a target application
app = Application().start("notepad.exe")
app.top_window().menu_select("Help->About Notepad") #to choose menu options
app.top_window().Ok.click()
app.top_window().Edit.type_keys("Hello world!", with_spaces=True)
