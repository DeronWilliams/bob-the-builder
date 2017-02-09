from PIL import Image
import os 

pics = Image.open("./Project1Images/1.png")
pics1 = Image.open("./Project1Images/2.png")
pics2 = Image.open("./Project1Images/3.png")
pics3 = Image.open("./Project1Images/4.png")
pics4 = Image.open("./Project1Images/5.png")
pics5 = Image.open("./Project1Images/6.png")
pics6 = Image.open("./Project1Images/7.png")
pics7 = Image.open("./Project1Images/8.png")
pics8 = Image.open("./Project1Images/9.png")# all my pictures

thelist=[pics, pics1, pics2, pics3, pics4, pics5, pics6, pics7, pics8]# pictures in a list


def median(thelist):# this is the real stuff that finds the median using the function
    median = 0
    sortedlist = sorted(thelist)
    lengthofthelist = len(sortedlist)
    centerofthelist = lengthofthelist / 2
    if len(sortedlist) == 1:
        for value in sortedlist:
            median += value
        return median

    elif len(sortedlist) % 2 == 0:
        temp = 0.0
        medianparties = []
        medianparties = sortedlist[centerofthelist -1 : centerofthelist +1 ]
        for value in medianparties:
            temp += value
            median = temp / 2
        return median

    else:
        medianpart = []
        medianpart = [sortedlist[centerofthelist]]
        for value in medianpart:
            median = value
        return median

picturewidth, pictureheight=thelist[0].size# this is the size of the picture

redpixellist=[]
greenpixellist=[]# the list and shades of colors of the picture
bluepixellist=[]

picture = Image.new("RGB", (picturewidth, pictureheight))

for x in range(picturewidth):# x and y lea
    for y in range(pictureheight):
        for myimage in thelist:
            myblue, mygreen, myred = myimage.getpixel((x,y))
            redpixellist.append(myred)
            greenpixellist.append(mygreen)
            bluepixellist.append(myblue)
            
        medianRed = median(redpixellist)
        medianGreen = median(greenpixellist)
        medianBlue = median(bluepixellist)
        
        picture.putpixel((x,y), (medianRed, medianGreen, medianBlue))
        
        redpixellist =[]
        greenpixellist =[]
        bluepixellist = []
        
        
    

picture.save("final.png")