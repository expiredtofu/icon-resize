from __future__ import print_function
import sys
import os.path
from PIL import Image
from Tkinter import Tk
from tkFileDialog import askopenfilename, askdirectory

Tk().withdraw()
print("Select image:")
imLocation = askopenfilename()
loop = True
comRes = [1024,512,152,144,120,114,100,80,76,72,58,57,50,40,29]
comName = ["iTunesArtwork@2x.png","iTunesArtwork.png",
           "Icon-76@2x.png","Icon-72@2x.png",
           "Icon-60@2x.png","Icon@2x.png",
           "Icon-Small-50@2x.png","Icon-Small-40@2x.png",
           "Icon-76.png","Icon-72.png",
           "Icon-Small@2x.png","Icon.png",
           "Icon-Small-50.png","Icon-Small-40.png",
           "Icon-Small.png"]

try:
    im = Image.open(imLocation)
    print("Image stats:", im.format, "%dx%d" % im.size, im.mode,"")
    xsize, ysize = im.size
    if xsize != ysize:
        print("Image not square, automatically cropping...")
        if xsize > ysize:
            im = im.crop(((xsize-ysize)/2,0,(xsize-ysize)/2+ysize,ysize))
        else:
            im = im.crop((0,(ysize-xsize)/2,xsize,(ysize-xsize)/2+xsize))
    print("Select an output directory: (caution: files will be overwritten automatically)")
    folder = askdirectory()
    if len(folder) == 0:
        loop = False
        print("invalid folder")
    while(loop):
        choice = raw_input("Please enter the width of the icon you want to export (enter \'a\' for Automatic, or \'q\' for quit): ")
        if choice.lower() == 'a':
            for i in range(len(comRes)):
                tempIm = im.resize((comRes[i],comRes[i]), Image.ANTIALIAS)
                tempIm.save(os.path.join(folder,comName[i]))
                print("Resized",str(comRes[i])+"x"+str(comRes[i]),"to file:",comName[i])
        elif choice.lower() == 'q':
            loop = False
        else:
            try:
                tempIm = im.resize((int(choice),int(choice)), Image.ANTIALIAS)
                fn = raw_input("Please enter the filename you want your icon to be, not including the extension (.JPG, .PNG): ")
                tempIm.save(os.path.join(folder,fn+'.'+'png'))
                print("Resized",str(choice)+"x"+str(choice),"to file:",fn+'.'+'png')
            except ValueError:
                print("Input not recognized, try again please.")
        print()
except IOError:
    print("invalid file")
    pass