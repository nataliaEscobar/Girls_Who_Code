from PIL import Image

##FUNCTIONS

def bw(pixel):

    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red + green + blue)//3 
    
    newRed = average
    if newRed > 255:
        newRed = 255
        

    newGreen = average
    if newGreen > 255:
        newGreen = 255
        
        
    newBlue = average
    if  newBlue > 255:
         newBlue = 255
         
    p = (newRed,newGreen,newBlue)

    newPixelList.append(p)

def doubleRed(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    newRed = red*2
    if newRed > 255:
        newRed = 255
        
    p = (newRed,green,blue)

    newPixelList.append(p)

def doubleBlue(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    newBlue = blue*2
    if newBlue > 255:
        newBlue = 255
        
    p = (red,green,newBlue)

    newPixelList.append(p)



##RUNNING CODE
#Import the image
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

length = len(pixelList)
oneThird = length//3
twoThird = oneThird*2

counter = 0

for pixel in pixelList:
    
    #pixel manipulation
    if (counter < oneThird): #this is the top half of the photo
        doubleRed(pixel)
    elif (counter < twoThird):
        bw(pixel)
    else: #this is the bottom half of the photo
        doubleBlue(pixel)
    counter = counter + 1
    



    #create new pixel



    #add pixel to the new pixel list
  

    


#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
#newImage.saver("newPhoto.jpeg","jpeg")




