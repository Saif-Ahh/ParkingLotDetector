import cv2
import cvzone
import pickle
import numpy as np

# constants
width = 70
height = 30

# check parking spaces
def checkParkingSpace(process_img) -> None:

    # Draw rectangles
    for pos in pos_list:
        x, y = pos[0], pos[1]

        # Crop image
        img_crop = process_img[y: y + height, x: x + width]
        count = cv2.countNonZero(img_crop)
        cvzone.putTextRect(parking_lot_img, str(count), (x, y+height-10), scale = 1.3, thickness=1, offset=0)

        # Color
        print(count)
        if count > 600:
            color = (255, 0, 0)
        else:
            color = (0, 255, 0)
        if pos[2] == 0:
            cv2.rectangle(parking_lot_img, (pos[0], pos[1]), (pos[0] + width, pos[1] + height), color, 2)
        elif pos[2] == 1:
            cv2.rectangle(parking_lot_img, (pos[0], pos[1]), (pos[0] + width, pos[1] + int(height / 2) + 10),
                          color, 2)

# Read video and read info
video_capture = cv2.VideoCapture('data\\parking_lot_video.mp4')
with open('data\\CarParkData', 'rb') as f:
    pos_list = pickle.load(f)

while True:
    # Loop video
    if video_capture.get(cv2.CAP_PROP_POS_FRAMES) == video_capture.get(cv2.CAP_PROP_FRAME_COUNT):
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, parking_lot_img = video_capture.read()
    if not success:
        break

    # Convert scale of image
    img_gray = cv2.cvtColor(parking_lot_img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 1)
    img_thres = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16) # Highlight car in white
    img_median = cv2.medianBlur(img_thres, 5)
    img_dialate = cv2.dilate(img_median, np.ones((3,3), np.uint8), iterations=1)
    checkParkingSpace(img_dialate)

    cv2.imshow('vid', parking_lot_img)
    cv2.waitKey(100)
