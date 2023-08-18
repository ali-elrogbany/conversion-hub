from PIL import Image
# from pdf2image import convert_from_path

class ConversionUtils:
    def __init__(self, filePath, noExtension):
        self.path = filePath
        self.pathWithoutExtension = noExtension

    def ConvertToJPG(self):
        img = Image.open(self.path)
        rgb_im = img.convert('RGB')
        rgb_im.save(f'{self.pathWithoutExtension}.jpg')

    def ConvertToPDF(self):
        img = Image.open(self.path)
        rgb_im = img.convert('RGB')
        rgb_im.save(f'{self.pathWithoutExtension}.pdf')

    def ConvertToPNG(self):
        img = Image.open(self.path)
        img.save(f'{self.pathWithoutExtension}.png')

    # def ConvertPDFToJPG(self):
    #     img = convert_from_path(self.path)
    #     for i in range(len(img)):
    #         img[i].save(f"Page {str(i)}.jpg")
        
    # def ConvertPDFToPNG(self):
    #     img = convert_from_path(self.path)
    #     for i in range(len(img)):
    #         img[i].save(f"Page {str(i)}.png")
        