import urllib.request
from PIL import Image


def imager(url, file_path, file_name):
    full_path = file_path + "\\" + file_name + ".jpg"
    urllib.request.urlretrieve(url, full_path)
    return full_path

def resizer(file_path):
    im = Image.open(file_path)
    width, height = im.size
    ratio = width/height
    if (ratio > 1.91) or (ratio < .8):
        if (ratio > 1.91):
            resized = im.resize((1080, 566))
            resized.save(file_path)
        if (ratio < .8):
            resized = im.resize((1080, 1350))
            resized.save(file_path)
        print("Resizer has resized")
    else:
        print("Nothing has been resizered")
    #can't be bigger than 1.91 ratio
    #can't be smaller than .8 ratio