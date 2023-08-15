from PIL import Image

class ConversionUtils:
    def __init__(self, filePath, noExtension):
        self.path = filePath
        self.pathWithoutExtension = noExtension

    def ConvertToJPG(self):
        img = Image.open(self.path)
        rgb_im = img.convert('RGB')
        rgb_im.save(f'{self.pathWithoutExtension}.jpg')