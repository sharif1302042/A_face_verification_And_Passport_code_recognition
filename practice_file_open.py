import cv2


src_path = "D:/project/final project/face-recognition-opencv/face-recognition-opencv/examples"


img = cv2.imread(src_path+"/example_01.png")

cv2.imshow("image",img)

cv2.waitKey(0)