# This program is written by Abubakr Shafique (abubakr.shafique@gmail.com) 
import os
import cv2 as cv
import numpy as np
import pydicom as PDCM

def Dicom_to_Image(Path):
    DCM_Img = PDCM.read_file(Path)

    rows = DCM_Img.get(0x00280010).value #Get number of rows from tag (0028, 0010)
    cols = DCM_Img.get(0x00280011).value #Get number of cols from tag (0028, 0011)

    Instance_Number = int(DCM_Img.get(0x00200013).value) #Get actual slice instance number from tag (0020, 0013)

    Window_Center = int(DCM_Img.get(0x00281050).value) #Get window center from tag (0028, 1050)
    Window_Width = int(DCM_Img.get(0x00281051).value) #Get window width from tag (0028, 1051)


    Window_Max = int(Window_Center + Window_Width / 2)
    Window_Min = int(Window_Center - Window_Width / 2)

    if (DCM_Img.get(0x00281052) is None):
        Rescale_Intercept = 0
    else:
        Rescale_Intercept = int(DCM_Img.get(0x00281052).value)

    if (DCM_Img.get(0x00281053) is None):
        Rescale_Slope = 1
    else:
        Rescale_Slope = int(DCM_Img.get(0x00281053).value)

    New_Img = np.zeros((rows, cols), np.uint8)
    Pixels = DCM_Img.pixel_array

    for i in range(0, rows):
        for j in range(0, cols):
            Pix_Val = Pixels[i][j]
            Rescale_Pix_Val = Pix_Val * Rescale_Slope + Rescale_Intercept

            if (Rescale_Pix_Val > Window_Max): #if intensity is greater than max window
                New_Img[i][j] = 255
            elif (Rescale_Pix_Val < Window_Min): #if intensity is less than min window
                New_Img[i][j] = 0
            else:
                New_Img[i][j] = int(((Rescale_Pix_Val - Window_Min) / (Window_Max - Window_Min)) * 255) #Normalize the intensities

    return New_Img, Instance_Number

def main():
    STUDY0_PATH_HRITVIK = "C:\\Users\\MAHE\\Desktop\\8th Sem Project\\Dicom_to_Image-Python-master\\Dicom_to_Image-Python-master\\STUDY0\\STUDY0"
    #STUDY0_PATH_HRITVIK = "STUDY0\\STUDY0"    #SERIES0 to SERIES26
    STUDY1_PATH_HRITVIK = "C:\\Users\\MAHE\\Desktop\\8th Sem Project\\Dicom_to_Image-Python-master\\Dicom_to_Image-Python-master\\STUDY1"
    #STUDY1_PATH_HRITVIK = "STUDY1"    #SERIES0 to SERIES16

    #Input_Folder = "C:\\Users\\MAHE\\Desktop\\STUDY0\\STUDY0\\SERIES8"
    Input_Folder = STUDY1_PATH_HRITVIK
    Output_Folder = "STUDY1_png_SLICES_"

    Input_Image_Lists = os.listdir(Input_Folder)
    print(Input_Image_Lists)
    for folder in Input_Image_Lists:
        input_folder = Input_Folder + '\\' + folder
        output_folder = Output_Folder + "_" + folder
        Input_Image_List = os.listdir(input_folder)

        if os.path.isdir(output_folder) is False:
            os.mkdir(output_folder)
        
        for i in range(0, len(Input_Image_List)):
            Output_Image, Instance_Number = Dicom_to_Image(input_folder + '/' + Input_Image_List[i])
            cv.imwrite(output_folder + '/' + str(Instance_Number - 1).zfill(4) + '.png', Output_Image)

    Input_Folder = STUDY0_PATH_HRITVIK
    Output_Folder = "STUDY0_png_SLICES_"

    Input_Image_Lists = os.listdir(Input_Folder)
    print(Input_Image_Lists)
    for folder in Input_Image_Lists:
        input_folder = Input_Folder + '\\' + folder
        output_folder = Output_Folder + "_" + folder
        Input_Image_List = os.listdir(input_folder)

        if os.path.isdir(output_folder) is False:
            os.mkdir(output_folder)
        
        for i in range(0, len(Input_Image_List)):
            Output_Image, Instance_Number = Dicom_to_Image(input_folder + '/' + Input_Image_List[i])
            cv.imwrite(output_folder + '/' + str(Instance_Number - 1).zfill(4) + '.png', Output_Image)

if __name__ == "__main__":
    main()