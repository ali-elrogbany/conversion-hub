import os
from tkinter import filedialog
from ConversionUtils import ConversionUtils

class File:
    def __init__(self):
        self.path = ""
        self.pathWithoutExtension = ""
        self.extension = ""
    
    def GetFilePath(self):
        # acceptedFileTypes = [("", ".png"), ("", ".jpeg"), ("", ".jpg"), ("", ".pdf")]
        acceptedFileTypes = [("images", ".png"), ("images", ".jpeg"), ("images", ".jpg")]
        path = filedialog.askopenfilename(filetypes=acceptedFileTypes)
        self.path = path
        return self.path
    
    def SplitPath(self):
        self.pathWithoutExtension, self.extension = os.path.splitext(self.path)
        return self.pathWithoutExtension, self.extension