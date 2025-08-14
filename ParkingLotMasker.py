import cv2
import pickle

width = 70
height = 30

# Add info from text file, if there is any
try:
    with open('data\\CarParkData', 'rb') as f:
        pos_list = pickle.load(f)
except:
    pos_list = []

# Add a box
def mouseClick(events, mouseX, mouseY, flags, params) -> None:
    # Add a box
    if events == cv2.EVENT_LBUTTONDOWN:
        pos_list.append((mouseX, mouseY, 0))
    elif events == cv2.EVENT_MBUTTONDOWN:
        pos_list.append((mouseX, mouseY, 1))
    # Remove a box
    elif events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(pos_list):
            x_pos, y_pos = pos[0], pos[1]
            if x_pos < mouseX < x_pos + width and y_pos < mouseY < y_pos + height:
                pos_list.pop(i)

    # Add info to text file
    with open('data\\CarParkData', 'wb') as f:
        pickle.dump(pos_list, f)

while True:
    # Read a screen and display it
    parking_lot_img = cv2.imread('data\\Parking_Lot_Mask.jpg')
    for pos in pos_list:
        if pos[2] == 0:
            cv2.rectangle(parking_lot_img, (pos[0], pos[1]), (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
        if pos[2] == 1:
            cv2.rectangle(parking_lot_img, (pos[0], pos[1]), (pos[0] + width, pos[1] + int(height / 2) + 10), (255, 0, 255), 2)
    cv2.imshow('image', parking_lot_img)
    cv2.setMouseCallback('image', mouseClick)
    cv2.waitKey(1)