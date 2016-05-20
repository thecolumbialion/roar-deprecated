#!/usr/bin/env python
from PIL import Image
#import matplotlib.pyplot as plt
import PIL
import os
import sys
def main(argv):
	#take original photos and resize them
	#print("I am here")
    #background = Image.open("Cover 2.png")
	background = Image.open(argv)
	originalFile = argv
	originalFileName = argv[7:]
	
	foreground = Image.open("images/LionCityCoverNoLogo.png")
	
	#resizeBackground = resize(background, "background.png", 2000)
	resizeForeground = resize(foreground, "foreground.png", 2048)
	resizeBackground = resizeH(background, "background.png")

	#resizeForeground = resizeH(foreground, "foreground.png")
	#time.sleep(.01)
	#open photos resized by height
	#backH = Image.open("background.png")
	#frontH = Image.open("foreground.png")
	#resizeBackgroundW = resizeW(backH, "background.png")
	#resizeForegroundW = resizeW(frontH, "foreground.png")
	#open newly resized photos
	back = Image.open("background.png")
	front = Image.open("foreground.png")

	#open lionlogo 
	lionlogo = Image.open("images/thecolumbialion.png")
	lionwidth, lionheight = lionlogo.size
	lionlogo = lionlogo.convert("RGBA")

	#lionlogo.show()
	#print(lionlogo.size)
	
	
	front = front.convert("RGBA")
	width, height = back.size
	print("width: " + str(width) + "length: " + str(height))



	back.paste(front, (0,0), front)	
	print(" place logo width: " + str(width -lionwidth) + "length: " + str(1300))
	#back.paste(lionlogo, (width - lionwidth, width - (width - lionwidth)), lionlogo)
	#back.paste(lionlogo, (width - lionwidth, height - lionheight), lionlogo)
	back.paste(lionlogo, ((width - lionwidth), 1300), lionlogo)
	#os.remove("images/" + argv[8:])
	filename = argv[8:] 
	back.save("images/wallpapers/" + filename[0:],"PNG")
	background.save("images/submitted/" + originalFileName, "PNG")
	#os.remove(background)
	os.remove("background.png")
	os.remove("foreground.png")
	os.remove(originalFile)
	print("------------------------")
	#os.remove("images/" + filename )
	#Image.open("../images/result.png")
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
def resizeW(image, name):
	basewidth = 2048
	img = image
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
	img.save(name)
	return img 

#resize the height to a set max of 1365 pixels
def resizeH(image, name):
    baseheight = 1365
    #img = Image.open(image)
    img = image
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    img.save(name)

    """#now resize the height
    img = Image.open(name)
    basewidth = 2048
    img = image
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img.save(name)"""
    return img	



if __name__ == "__main__":
    main(sys.argv[1])


#code graveyard
#foreground.show() 
	#background = background.convert("RGBA")
	#new_img = Image.blend(background, overlay, 0.3)
#new_img = Image.alpha_composite(background, overlay
	#background.show()
	#Image.alpha_composite(background, foreground).save("result.png", "PNG")
