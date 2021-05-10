import numpy as np
import matplotlib.pyplot as plt
import cv2
  
  
# Read in the image
image = cv2.imread("C:\\Users\\MAHE\\Desktop\\8th Sem Project\\Dicom_to_Image-Python-master\\Dicom_to_Image-Python-master\\pseudoushamax.png")
  
# Change color to RGB (from BGR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Reshaping the image into a 2D array of pixels and 3 color values (RGB)
pixel_vals = image.reshape((-1,2))
  
# Convert to float type
pixel_vals = np.float32(pixel_vals)
  
plt.imshow(image)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
  
# then perform k-means clustering wit h number of clusters defined as 3
#also random centres are initally chosed for k-means clustering
k = 5
retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  
# convert data into 8-bit values
centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]
  
# reshape data into the original image dimensions
segmented_image = segmented_data.reshape((image.shape))
  
plt.imshow(segmented_image)
