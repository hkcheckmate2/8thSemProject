# Import the necessary libraries
from PIL import Image
from numpy import asarray
import numpy
import math
#import morphologicalGAC
import multiply_masks

def probGauss(x,mu,sigma):
	ans = (math.e)**(-0.5*((x-mu)/sigma)**2)
	return ans

#print(probGauss(340,336,60))
"""
The following script contains functions for the following transformations:
1) image to numpy array
2) numpy array to transformed matrix (after parsing via polynomial)
3) matrix to recreated image
"""

def poly(pixel):
	#return max((1947*pixel - 11.39*pixel + 0.0169*pixel*pixel),255)
	return (1947*pixel - 11.39*pixel + 0.0169*pixel*pixel)

def bigpoly(pixel):
	a = [11.80174727, -25490.80609, 1.48E+06, -3.77E+07, 5.66E+08, -5.63E+09, 3.93E+10, -1.98E+11, 7.21E+11]
	a += [-1.89E+12, 3.39E+12, -3.71E+12, 1.31E+12, 2.17E+12, -2.28E+12, -1.21E+12, 2.18E+12, 1.09E+12, -1.83E+12]
	a += [-1.33E+12, 1.32E+12, 1.58E+12, -7.55E+11, -1.68E+12, 3.41E+11, 1.68E+12, -3.82E+11, -1.66E+12, 1.66E+12]
	a += [-6.57E+11, 1.00E+11]
	#a is our test polynomial
	ans = 0
	for i in range(len(a)):
		ans += a[i]*(pixel**i)
	return ans

def imgToNumpy(path):  
	# load the image and convert into numpy array
	img = Image.open(path)
	numpydata = asarray(img)
	#print(numpydata.shape)
	print("Image to Numpy Array executed")
	return numpydata

def filter(x):
	return x if (x>270 and x<430) else 0

def transformNumpyToMartix(numpydata,func):
	mat = [[0 for x in range(len(numpydata))] for y in range(len(numpydata[0]))]
	# data
	for x in range(len(numpydata)):
	    for y in range(len(numpydata[0])):
	        #mat[x][y] += int(numpydata[x][y]*0.3) <=== FOR CHECKING BRIGHTNESS CHANGE IN O/P
	        l = len(numpydata)
	        t = probGauss(y,l/2 - 10,40)
	        #t = 1
	        mat[x][y] += int(t*func(numpydata[x][y]/255) + (1-t)*numpydata[x][y])
	        mat[x][y] *= 255
	        #print(mat[x][y])
	print("Numpy Array Transformation Completed")
	return mat

def TransformNumpyToMartix(numpydata,func):
	mat = [[0 for x in range(len(numpydata))] for y in range(len(numpydata[0]))]
	for x in range(len(numpydata)):
	    for y in range(len(numpydata[0])):
	        l = len(numpydata)
	        t = probGauss(y,l/2,60)
	        mat[x][y] = 255*numpydata[x][y]
	        if multiply_masks.final_3x4x6[x][y]:
	        	mat[x][y] = 255*int(t*func(numpydata[x][y]/275) + (1-t)*numpydata[x][y])
	print("Numpy Array Transformation Completed")
	return mat
    
def matrixToImg(mat,target_path):
	imgarr = numpy.array(mat)
	imga = Image.fromarray(imgarr)
	imga.show()
	#imga = Image.fromarray(imgarr*255)
	imga.save(target_path)
	#imga.show()
	print(imga)
	print("Transformed Matrix to Image Synthesis completed")
	return imgarr

#for row in numpydata:
#	for pixel in row:
#		print(pixel," => "),
#		pixel = poly(pixel)
#		print(pixel)

#print(numpy.max(numpydata))
#print(numpy.min(numpydata))
#img = Image.fromarray(numpydata)
#img.save('ct.png')
#img.show()

def main():
	image_path = "C:\\Users\\MAHE\\Desktop\\8th Sem Project\\Dicom_to_Image-Python-master\\Dicom_to_Image-Python-master\\Series13_png\\0012.png"
	#image_path = "C:\\Users\\MAHE\\Desktop\\8th Sem Project\\Dicom_to_Image-Python-master\\Dicom_to_Image-Python-master\\Series8_png\\0018.png"
	numpy_for_image = imgToNumpy(image_path)
	print(numpy_for_image)
	transformed_matrix = TransformNumpyToMartix(numpy_for_image,poly)
	#transformed_matrix = transformNumpyToMartix(numpy_for_image,poly)
	#print(transformed_matrix)
	modified_numpy = matrixToImg(transformed_matrix,"pseudo_merged_mask3_1.png")
	#pseudo_(mean value)_(null for no shift else L for left R for rigt followed by value)_(standard deviation)
	print(modified_numpy)

if __name__ == "__main__":
    main()