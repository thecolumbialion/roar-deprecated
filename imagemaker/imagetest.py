#!/usr/bin/env python
from PIL import Image
#import matplotlib.pyplot as plt
import PIL
import os
import sys
def main(argv):
	background = Image.open(argv)
	originalFile = argv
	originalFileName = argv[7:]
	foreground = Image.open("images/LionCityCoverNoLogo.png")
	resizeForeground = resize(foreground, "foreground.png", 2048)
	resizeBackground = resizeH(background, "background.png")

	back = Image.open("background.png")
	front = Image.open("foreground.png")

	#open lionlogo 
	lionlogo = Image.open("images/thecolumbialion.png")
	lionwidth, lionheight = lionlogo.size
	lionlogo = lionlogo.convert("RGBA")

	front = front.convert("RGBA")
	width, height = back.size

	back.paste(front, (0,0), front)	
	back.paste(lionlogo, ((width - lionwidth), 1300), lionlogo)

	filename = argv[8:] 
	back.save("images/wallpapers/" + filename[0:],"PNG")
	background.save("images/submitted/" + originalFileName, "PNG")
	#os.remove(background)
	os.remove("background.png")
	os.remove("foreground.png")
	os.remove(originalFile)

	return filename

#resize based on desired photo width
def resize(image, name, size):
	basewidth = size
	img = image
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
	img.save(name)
	return img 

#resize image based on a set width
"""def resizeW(image, name):
	basewidth = 2048
	img = image
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
	img.save(name)
	return img """

#resize the height to a set max of 1365 pixels
def resizeH(image, name):
    baseheight = 1365
    #img = Image.open(image)
    img = image
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    img.save(name)
    return img	



if __name__ == "__main__":
    main(sys.argv[1])

