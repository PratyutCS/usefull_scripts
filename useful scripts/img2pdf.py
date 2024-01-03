from os import listdir
from PIL import Image

mypath = "C:/Users/praty/OneDrive/Desktop/p2d"

ndir = [mypath+"/"+f for f in listdir(mypath)]

images = [Image.open(f)for f in ndir]

save = "C:/Users/praty/OneDrive/Desktop/p2d/000000merge.pdf"
    
images[0].save(save, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])