
STUDY0_PATH = "C:\\Users\\MAHE\\Desktop\\8th Sem Project\\Dicom_to_Image-Python-master\\Dicom_to_Image-Python-master\\STUDY0\\STUDY0"
#SERIES0 to SERIES26
STUDY1_PATH = "C:\\Users\\MAHE\\Desktop\\8th Sem Project\\Dicom_to_Image-Python-master\\Dicom_to_Image-Python-master\\STUDY1"
#SERIES0 to SERIES16
TEST_DICOM_DATA = "C:\\Users\\MAHE\\Desktop\\8th Sem Project\\Dicom_to_Image-Python-master\\Dicom_to_Image-Python-master\\Data\\bbmri-53323131.dcm"
#brain mri scan
STUDY0_SERIES = []
STUDY1_SERIES = []

for var0 in range(27):
	STUDY0_SERIES.append(STUDY0_PATH + "\\SERIES" + str(var0))
	#print(STUDY0_SERIES[var0])

for var1 in range(17):
	STUDY1_SERIES.append(STUDY1_PATH + "\\SERIES" + str(var1))
	#print(STUDY1_SERIES[var1])

def main():
	for var0 in range(27):
		print(STUDY0_SERIES[var0])

	for var1 in range(17):
		print(STUDY1_SERIES[var1])

if __name__ == "__main__":
    main()