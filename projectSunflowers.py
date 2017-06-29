from PIL import Image

#Import the image
myImage = Image.open("sunflower.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

length = len(pixelList)

darkBlue =(0,51,76)
red = (217,26,33)
lightBlue = (112,150,158)
yellow = (252,227,266)



for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    intensity = (red + blue + green)
    
    #pixel manipulation
    if (intensity < 182):
       newPixelList.append(darkBlue)
    elif (182 < intensity and 364 > intensity):
        newPixelList.append(red)
    elif (364 < intensity and 546 > intensity):
        newPixelList.append(lightBlue)
    else:
        newPixelList.append(yellow)

        
    


#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
#newImage.saver("newPhoto.jpeg","jpeg")

