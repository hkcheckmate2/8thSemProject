def main():
	#image_path = "C:\\Users\\MAHE\\Desktop\\8th Sem Project\\Dicom_to_Image-Python-master\\Dicom_to_Image-Python-master\\Series13_png\\0012.png"
	image_path = input()
	numpy_for_image = imgToNumpy(image_path)
	print(numpy_for_image)
	transformed_matrix = transformNumpyToMartix(numpy_for_image,poly)
	#print(transformed_matrix)
	modified_numpy = matrixToImg(transformed_matrix,"pseudax.png")
	print(modified_numpy)

if __name__ == "__main__":
    main()