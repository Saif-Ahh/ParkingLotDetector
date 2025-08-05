import cv2

while True:
    # Read a screen and display it
    parking_lot_img = cv2.imread('data\\Parking_Lot_Mask.jpg')
    cv2.imshow('image', parking_lot_img)
    cv2.waitKey(1)
