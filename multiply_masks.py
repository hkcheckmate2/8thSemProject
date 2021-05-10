from PIL import Image
from numpy import asarray
import numpy
import math

def imgToNumpy(path):  
	# load the image and convert into numpy array
	img = Image.open(path)
	numpydata = asarray(img)
	#print(numpydata.shape)
	print("Image to Numpy Array executed")
	return numpydata

def transformNumpyToMartix(numpydata):
	mat = [[0 for x in range(len(numpydata))] for y in range(len(numpydata[0]))]
	# data
	for x in range(len(numpydata)):
	    for y in range(len(numpydata[0])):
	        mat[x][y] = numpydata[x][y]
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

def multiply_images(PATH_IMG1,PATH_IMG2,PATH_IMG3):
	#PATH_IMG1 = 'mask3.png'
	numpy_for_image3 = imgToNumpy(PATH_IMG1)
	image1 = transformNumpyToMartix(numpy_for_image3)
	#PATH_IMG2 = 'mask4.png'
	numpy_for_image4 = imgToNumpy(PATH_IMG2)
	image2 = transformNumpyToMartix(numpy_for_image4)
	#PATH_IMG3 = 'mask6.png'
	numpy_for_image6 = imgToNumpy(PATH_IMG3)
	image3 = transformNumpyToMartix(numpy_for_image6)

	morphed_array = []
	for x in range(len(image1)):
		row = []
		for y in range(len(image1[0])):
			row.append(-1*(image1[x][y])*(image2[x][y])*(image3[x][y]))
		morphed_array.append(row)

	print(morphed_array)
	final = matrixToImg(morphed_array,"merged_mask_3x4x6.png")
	#print(image1)
	#print(image2)
	print(final)
