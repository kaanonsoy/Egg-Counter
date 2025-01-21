import cv2
import numpy as np
import imutils

lower_orange = np.array([5, 50, 50])  # Lower limit for orange color
upper_orange = np.array([180, 255, 255])  # Upper limit for orange color

lower_brown = np.array([5, 50, 50])  # Lower limit for brown color
upper_brown = np.array([25, 200, 150])  # Upper limit for brown color

egg_columns = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
space = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

cap = cv2.VideoCapture("C:/Users/YUSUF ÖNSOY/OneDrive/Masaüstü/EggDetection-master/EggDetection-master/yum2.mp4")  # Sample video # If you want to use a camera, write "0"

fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)) 
eggs_counter = 0 
frame_counter = 0 

while True:
    ret, image = cap.read()

    if not ret:    
        break
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    image = imutils.resize(image, width=640)  
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
    
    # Creating masks for orange and brown colors
    maskOrange = cv2.inRange(imageHSV, lower_orange, upper_orange)
    maskBrown = cv2.inRange(imageHSV, lower_brown, upper_brown)

    # Combining the masks
    mask = cv2.bitwise_or(maskOrange, maskBrown)

    # Processing the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.erode(mask, kernel, iterations=5)
    mask = cv2.dilate(mask, None, iterations=3)

    area_pts = np.array([[55, 50], [imageHSV.shape[1] - 25, 50], [imageHSV.shape[1] - 25, 110], [55, 110]])

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]  

    # Analyzing the position of the eggs
    for cnt in cnts:
        x, y, w, h = cv2.boundingRect(cnt)  
        if (cv2.contourArea(cnt) > 15) and (50 < (y + h) < 130): 
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radio = 2  
            if 75 < int(y) < 84: 
                    if (55 < int(x) <= 95) and (space[0] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[0] = 1
                        egg_columns[0] = frame_counter

                    if (95 < int(x) <= 135) and (space[1] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[1] = 1
                        egg_columns[1] = frame_counter

                    if (135 < int(x) <= 175) and (space[2] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[2] = 1
                        egg_columns[2] = frame_counter

                    if (175 < int(x) <= 215) and (space[3] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[3] = 1
                        egg_columns[3] = frame_counter

                    if (215 < int(x) <= 255) and (space[4] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[4] = 1
                        egg_columns[4] = frame_counter

                    if (255 < int(x) <= 295) and (space[5] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[5] = 1
                        egg_columns[5] = frame_counter

                    if (295 < int(x) <= 335) and (space[6] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[6] = 1
                        egg_columns[6] = frame_counter

                    if (335 < int(x) <= 375) and (space[7] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[7] = 1
                        egg_columns[7] = frame_counter

                    if (375 < int(x) <= 415) and (space[8] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[8] = 1
                        egg_columns[8] = frame_counter

                    if (415 < int(x) <= 455) and (space[9] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[9] = 1
                        egg_columns[9] = frame_counter

                    if (455 < int(x) <= 495) and (space[10] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[10] = 1
                        egg_columns[10] = frame_counter

                    if (495 < int(x) <= 540) and (space[11] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[11] = 1
                        egg_columns[11] = frame_counter

                    if (535 < int(x) <= 535) and (space[12] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[12] = 1
                        egg_columns[12] = frame_counter

                    if (535 < int(x) <= 535) and (space[13] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[13] = 1
                        egg_columns[13] = frame_counter

                    if (535 < int(x) <= 535) and (space[14] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[14] = 1
                        egg_columns[14] = frame_counter
                    
                    if (535 < int(x) <= 535) and (space[15] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[15] = 1
                        egg_columns[15] = frame_counter

                    if radius > 30:
                        radius
                        eggs_counter = eggs_counter + 1
                     
    # Checking empty spaces
    index = 0
    for i in egg_columns:
        if((frame_counter - i) > 10):
            space[index] = 0
        index += 1

    frame_counter = frame_counter + 1
    cv2.drawContours(image, [area_pts], -2, (255, 0, 255), 2)  # Rectangle
    cv2.line(image, (55, 50), (55, 110), (0, 255, 255), 1)  # 1
    cv2.line(image, (95, 50), (95, 110), (0, 255, 255), 1)  # 2
    cv2.line(image, (135, 50), (135, 110), (0, 255, 255), 1)  # 3
    cv2.line(image, (175, 50), (175, 110), (0, 255, 255), 1)  # 4
    cv2.line(image, (215, 50), (215, 110), (0, 255, 255), 1)  # 5
    cv2.line(image, (255, 50), (255, 110), (0, 255, 255), 1)  # 6
    cv2.line(image, (295, 50), (295, 110), (0, 255, 255), 1)  # 7
    cv2.line(image, (335, 50), (335, 110), (0, 255, 255), 1)  # 8
    cv2.line(image, (375, 50), (375, 110), (0, 255, 255), 1)  # 9
    cv2.line(image, (415, 50), (415, 110), (0, 255, 255), 1)  # 10
    cv2.line(image, (455, 50), (455, 110), (0, 255, 255), 1)  # 11
    cv2.line(image, (495, 50), (495, 110), (0, 255, 255), 1)  # 12
    cv2.line(image, (535, 50), (535, 110), (0, 255, 255), 1)  # 13
    cv2.line(image, (575, 50), (575, 110), (0, 255, 255), 1)  # 14
    cv2.line(image, (615, 50), (615, 110), (0, 255, 255), 1)  # 15
    cv2.line(image, (55, 80), (image.shape[1] - 25, 80), (0, 255, 255), 1)  # Center line
    
    cv2.imshow("image", image)

    key = cv2.waitKey(1)
    if key == 27:  # Exit the code by pressing ESC
        break

cap.release()
cv2.destroyAllWindows()

print("Total Number of Eggs:", eggs_counter)
