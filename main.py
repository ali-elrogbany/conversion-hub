from tkinter import *
from FileUtilities import *

window = Tk()
window.title('Conversion Hub')

title = Label(window, text = "Conversion Hub")
title.pack()

fileUtils = File()
browseFileButton = Button(window, text = 'Browse Files', width = 25, command = fileUtils.GetFilePath)
browseFileButton.pack()

window.mainloop()

