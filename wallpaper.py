import os
import PIL
from shutil import copyfile
from PIL import Image


picture_path = r"D:\sex\pics"
wallpaper_path = r"D:\sex\wallpaper"
try:
    os.mkdir(wallpaper_path)
except FileExistsError as e:
    print(e)
    

for root, dirs, files in os.walk(picture_path):
    for file in files:
        try:
            img = Image.open(root + "\\" + file)
        except PIL.UnidentifiedImageError as e:
            print(e)
            continue
            
        
        if img.size[0] / img.size[1] > 1.7:
            copyfile(root + "\\" + file, wallpaper_path + "\\" + file)

            
