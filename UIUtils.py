from tkinter import *
from PIL import Image, ImageTk

from FileUtilities import *
from ConversionUtils import *

class UI:
    def __init__(self, master):
        self.master = master
        self.title = Label(self.master, text = "Conversion Hub")
        self.title.place(relx = 0.5, rely = 0.05, anchor = 'center')

        self.fileUtils = File()
        self.browseFileButton = Button(self.master, text = 'Browse Files', width = 25, command = self.OnFileUploaded)
        self.browseFileButton.place(relx = 0.5, rely = 0.5, anchor = 'center')

        self.filePath = ""
        self.pathNoExtension = ""
        self.fileExtension = ""

    def OnFileUploaded(self):
        self.filePath = self.fileUtils.GetFilePath()
        self.pathNoExtension, self.fileExtension = self.fileUtils.SplitPath()

        self.converter = ConversionUtils(self.filePath, self.pathNoExtension)
        
        self.browseFileButton.place_forget()

        load = Image.open(self.filePath)
        load.thumbnail((200, 112.5), Image.Resampling.LANCZOS)
        render = ImageTk.PhotoImage(load)
        img = Label(self.master, image=render)
        img.image = render
        img.place(relx = 0.5, rely = 0.25, anchor = 'center')

        self.convertTitle = Label(self.master, text = "Convert To:")
        self.convertTitle.place(relx = 0.5, rely = 0.70, anchor = 'center')

        if self.fileExtension == ".png":
            self.convertToJpgButton = Button(self.master, text = 'JPG', width = 10, command = self.converter.ConvertToJPG)
            self.convertToJpgButton.place(relx = 0.5, rely = 0.75, anchor = 'center')

            self.convertToPdfButton = Button(self.master, text = 'PDF', width = 10, command = self.converter.ConvertToPDF)
            self.convertToPdfButton.place(relx = 0.5, rely = 0.80, anchor = 'center')

