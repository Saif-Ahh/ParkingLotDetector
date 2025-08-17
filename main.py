import cv2

# Read video
video_capture = cv2.VideoCapture('data\\parking_lot_video.mp4')

while True:
    success, parking_lot_img = video_capture.read()
    if not success:
        break

    cv2.imshow('vid', parking_lot_img)
    cv2.waitKey(100)
