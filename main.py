import cv2

# To generate random color rectangles around faces
from random import randrange

# load some pre trained data on face frontals from opencv  (haar cascade algorith)
face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# choose an image to detect faces
# img = cv2.imread('vpic2.png')
#img = cv2.imread('bts2.jpg')

# Must convert to gray scale
# gray_scaleimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces
# face_coordinates = face_data.detectMultiScale(gray_scaleimg)
# print(face_coordinates)

# Draw rectangle around the face
# cv2.rectangle(img,(x,y),(x+width,y+height),(RBG==opencv -> B,G,R),(width of sq box))
'''
cv2.rectangle(img, (61, 113), (587, 639), (0,255,0), 2)

aacording to above line of code we are mentioning the coordinates of face directly 
'''

'''
# Automatic coordinates detection when there is one person in image
(x, y, w, h) = face_coordinates[0]
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Face detection for 2nd person in the image
(x, y, w, h) = face_coordinates[1]
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Face detection for 3rd person in the image
(x, y, w, h) = face_coordinates[2]
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Face detection for 4th person in the image
(x, y, w, h) = face_coordinates[3]
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

sloppy way od doing it 

'''

'''
# Automatic faces detection using loop
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256),
                  randrange(256), randrange(255)), 3)

# show image
cv2.imshow("image", img)
cv2.waitKey()

'''


# To capture video from webcam
webcam = cv2.VideoCapture(0)
# 0 means default webcam or if i give the path of the video it will capture faces on that

# Iterate forever over the frames
while True:
    # Read the current frames
    successful_frame_read, frame = webcam.read()

    # Must convert the frame to grayscale
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    face_coordinates = face_data.detectMultiScale(grayscale_frame)
    # print(face_coordinates)

    # Automatic faces detection using loop
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256),
                                                  randrange(256), randrange(255)), 3)

    cv2.imshow("image", frame)
    key = cv2.waitKey(1)

    # Stop if Q is pressed
    if key == 81 or key == 113:
        break

# Release the videocapture Object
webcam.release()


print("Code completed")
