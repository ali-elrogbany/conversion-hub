import os
from tkinter import filedialog
from ConversionUtils import ConversionUtils

class File:
    def __init__(self):
        self.path = ""
        self.pathWithoutExtension = ""
        self.extension = ""
    
    def GetFilePath(self):
        path = filedialog.askopenfilename(filetypes=[("image", ".png")])
        self.path = path

        self.pathWithoutExtension, self.extension = os.path.splitext(self.path)
        
        self.Convert()
        print(f'file path: {self.path}, path without extension: {self.pathWithoutExtension}, extension: {self.extension}')
        
    def Convert(self):
        conversionUtils = ConversionUtils(self.path, self.pathWithoutExtension)
        conversionUtils.ConvertToJPG()