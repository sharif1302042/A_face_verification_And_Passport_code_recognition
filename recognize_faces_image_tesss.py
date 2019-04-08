# USAGE
# python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png 

# import the necessary packages
from testImageFromDisk import get_string
import face_recognition
import argparse
import pickle
import cv2


#imgpath = "D:/project/final project/face-recognition-opencv/face-recognition-opencv - test/examples/example_04.png"

# load the input image and convert it from BGR to RGB
#image = cv2.imread(imgpath)

src_path = "D:/project/final project/codes"

def string_match(name):
	img = cv2.imread(src_path+ "/" + name + ".png")

	cv2.imshow("image",img)

	res= get_string(img)
	#print (res)
	return res


	cv2.waitKey(0)





def recognize_face(image ,a1):
	# load the known faces and embeddings
	print("[INFO] loading encodings...")
	data = pickle.loads(open("encodings.pickle", "rb").read())

	
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# detect the (x, y)-coordinates of the bounding boxes corresponding
	# to each face in the input image, then compute the facial embeddings
	# for each face
	print("[INFO] recognizing faces...")
	boxes = face_recognition.face_locations(rgb,
		model= "cnn")
	encodings = face_recognition.face_encodings(rgb, boxes)

	# initialize the list of names for each face detected
	names = []
	found = False

	# loop over the facial embeddings
	for encoding in encodings:
		# attempt to match each face in the input image to our known
		# encodings
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Unknown"

		# check to see if we have found a match
		if True in matches:
			found = True
			# find the indexes of all matched faces then initialize a
			# dictionary to count the total number of times each face
			# was matched
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			# loop over the matched indexes and maintain a count for
			# each recognized face face
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			# determine the recognized face with the largest number of
			# votes (note: in the event of an unlikely tie Python will
			# select first entry in the dictionary)
			name = max(counts, key=counts.get)
		
		# update the list of names
		names.append(name)

	# loop over the recognized faces
	for ((top, right, bottom, left), name) in zip(boxes, names):
		# draw the predicted face name on the image
		print (name)
		
		if(name):
			a2 = string_match(name)

		else: 
			a2= "name"
		print (a2)

		if(a1 == a2):
			print ("match found")
			cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
			y = top - 15 if top - 15 > 15 else top + 15
			cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
				0.75, (0, 255, 0), 2)
		else:
			print("image didn't match")
			cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
			y = top - 15 if top - 15 > 15 else top + 15
			cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			0.75, (0, 0, 255), 2)

	# show the output image
	if(found): 
		cv2.imshow(a1, image)
		cv2.imwrite("D:/project/final project/images/not_match.png",image)
	else:
		print("no match found")
		print("no match found")
	cv2.waitKey(0)

#recognize_face(image)