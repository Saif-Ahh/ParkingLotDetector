import cv2

# Read video
video_capture = cv2.VideoCapture('data\\parking_lot_video.mp4')

while True:
    # Loop video
    if video_capture.get(cv2.CAP_PROP_POS_FRAMES) == video_capture.get(cv2.CAP_PROP_FRAME_COUNT):
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, parking_lot_img = video_capture.read()
    if not success:
        break

    cv2.imshow('vid', parking_lot_img)
    cv2.waitKey(100)
