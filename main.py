from tkinter import *
from FileUtilities import *
from UIUtils import *


master = Tk()
master.title('Conversion Hub')
master.geometry("350x500")
master.resizable(False, False)

ui = UI(master = master)

master.mainloop()