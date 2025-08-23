import cv2
import pickle

# constants
width = 70
height = 30

# check parking spaces
def checkParkingSpace() -> None:

    # Draw rectangles
    for pos in pos_list:
        if pos[2] == 0:
            cv2.rectangle(parking_lot_img, (pos[0], pos[1]), (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
        elif pos[2] == 1:
            cv2.rectangle(parking_lot_img, (pos[0], pos[1]), (pos[0] + width, pos[1] + int(height / 2) + 10),
                          (255, 0, 255), 2)

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
    checkParkingSpace()

    cv2.imshow('vid', parking_lot_img)
    cv2.waitKey(100)
