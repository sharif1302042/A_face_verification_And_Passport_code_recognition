
from testImageFromDisk import get_string
import cv2


src_path = "D:/project/final project/codes"

def string_match(name):
	img = cv2.imread(src_path+ "/" + name + ".png")

	cv2.imshow("image",img)

	res= get_string(img)
	print (res)


	cv2.waitKey(0)


a1 = string_match("1")
a2 = string_match("1")
if(a1 == a2):
	print ("same")
else:
	print("no")