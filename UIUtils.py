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

        self.convertToJpgButton = None
        self.convertToPdfButton = None
        self.convertToPngButton = None

    def OnFileUploaded(self):
        self.filePath = self.fileUtils.GetFilePath()
        self.pathNoExtension, self.fileExtension = self.fileUtils.SplitPath()

        self.converter = ConversionUtils(self.filePath, self.pathNoExtension)
        
        self.browseFileButton.place_forget()

        if self.fileExtension != ".pdf":
            load = Image.open(self.filePath)
            load.thumbnail((200, 112.5), Image.Resampling.LANCZOS)
            render = ImageTk.PhotoImage(load)
            self.img = Label(self.master, image=render)
            self.img.image = render
            self.img.place(relx = 0.5, rely = 0.25, anchor = 'center')

        self.convertTitle = Label(self.master, text = "Convert To:")
        self.convertTitle.place(relx = 0.5, rely = 0.70, anchor = 'center')

        if self.fileExtension == ".png":
            self.convertToJpgButton = Button(self.master, text = 'JPG', width = 10, command = lambda: [self.converter.ConvertToJPG(), self.OnConvertButtonClicked()])
            self.convertToJpgButton.place(relx = 0.5, rely = 0.75, anchor = 'center')

            self.convertToPdfButton = Button(self.master, text = 'PDF', width = 10, command = lambda: [self.converter.ConvertToPDF(), self.OnConvertButtonClicked()])
            self.convertToPdfButton.place(relx = 0.5, rely = 0.80, anchor = 'center')

        if self.fileExtension == ".jpg" or self.fileExtension == ".jpeg":
            self.convertToPngButton = Button(self.master, text = 'PNG', width = 10, command = lambda: [self.converter.ConvertToPNG(), self.OnConvertButtonClicked()])
            self.convertToPngButton.place(relx = 0.5, rely = 0.75, anchor = 'center')

            self.convertToPdfButton = Button(self.master, text = 'PDF', width = 10, command = lambda: [self.converter.ConvertToPDF(), self.OnConvertButtonClicked()])
            self.convertToPdfButton.place(relx = 0.5, rely = 0.80, anchor = 'center')

        # if self.fileExtension == ".pdf":
        #     self.convertToPngButton = Button(self.master, text = 'PNG', width = 10, command = self.converter.ConvertPDFToPNG)
        #     self.convertToPngButton.place(relx = 0.5, rely = 0.75, anchor = 'center')

        #     self.convertToJpgButton = Button(self.master, text = 'JPG', width = 10, command = self.converter.ConvertPDFToJPG)
        #     self.convertToJpgButton.place(relx = 0.5, rely = 0.80, anchor = 'center')

    def OnConvertButtonClicked(self):
        self.convertTitle.place_forget()

        self.doneTitle = Label(self.master, text = "Conversion Complete")
        self.doneTitle.place(relx = 0.5, rely = 0.70, anchor = 'center')

        self.mainMenuButton = Button(self.master, text = "Main Menu", width = 10, command = self.GetMainMenu)
        self.mainMenuButton.place(relx = 0.5, rely = 0.75, anchor = 'center')

        self.exitButton = Button(self.master, text = "Exit", width = 10, command = self.master.destroy)
        self.exitButton.place(relx = 0.5, rely = 0.80, anchor = 'center')
        
        if self.convertToJpgButton:
            self.convertToJpgButton.place_forget()

        if self.convertToPdfButton:
            self.convertToPdfButton.place_forget()

        if self.convertToPngButton:
            self.convertToPngButton.place_forget()

    def GetMainMenu(self):
        if self.img:
            self.img.place_forget()

        if self.doneTitle:
            self.doneTitle.place_forget()

        if self.mainMenuButton:
            self.mainMenuButton.place_forget()

        if self.exitButton:
            self.exitButton.place_forget()

        self.browseFileButton.place(relx = 0.5, rely = 0.5, anchor = 'center')
