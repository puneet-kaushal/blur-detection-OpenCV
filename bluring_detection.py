import cv2 #opencv is imported
from tkinter import Tk # Module to fetch the images graphically
from tkinter import filedialog
toplevel = Tk()
toplevel.withdraw()
filename = filedialog.askopenfilename()   #fetch the path of the image
image = cv2.imread(filename)   # read the image

#calculate laplacian of the image
def variance_of_laplacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()
#converting the image into the grayscale
def rgb2gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#comparing with the threshold
def threshold(value,filename):
    threshold_val= 100
    if value > threshold_val:
        print(filename+ " This image is Not Blurry: " + str(value))
    else:
        print(filename+ "This image is Blurry: " + str(value))

gray_image = rgb2gray(image)
variance_laplacian = variance_of_laplacian(gray_image)
output = threshold(variance_laplacian,filename)












