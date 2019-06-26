import numpy as np
import cv2
import time


def detect_LED_green(inImg):
    rects = []
    w = inImg.shape[1]
    h = inImg.shape[0]
    
    if h < 100:
        scale = 2
    else:
        scale = 1

    #cv2.imshow('input', inImg)
    #cv2.waitKey(2)
    
    resizeImg = cv2.resize(inImg, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)

    hsv_img = cv2.cvtColor(resizeImg, cv2.COLOR_BGR2HSV)

    low_range1 = np.array([60, 100, 60])
    high_range1 = np.array([96, 255, 255])
    th1 = cv2.inRange(hsv_img, low_range1, high_range1)
    dilated = cv2.dilate(th1, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8)), iterations=2)
    #cv2.imshow('green', dilated)
    #cv2.waitKey(2)

    #dst = cv2.addWeighted(dilated, 0.5, dilated1, 0.5, 0);

    img = cv2.medianBlur(dilated, 5)
    
    
    #th2 = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
  
    circles = [[0,0,0]] 
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=100,param2=10,minRadius=12,maxRadius=40) #10,40
    #circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=80,param2=30,minRadius=10,maxRadius=40) #10,40

    #circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,50,param1=80,param2=30,minRadius=10,maxRadius=50)

    #print (circles)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
    else:
        print("cannot get valid value!")
    
    #if circles != None: 
    #if circles :
    
    #print ("green circle is:",circles)
    
    return circles

def detect_LED_red(inImg):

    rects = []
    w = inImg.shape[1]
    h = inImg.shape[0]
    
    if h < 100:
        scale = 2
    else:
        scale = 1

    #cv2.imshow('input', inImg)
    #cv2.waitKey(2)
    
    resizeImg = cv2.resize(inImg, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)

    hsv_img = cv2.cvtColor(resizeImg, cv2.COLOR_BGR2HSV)

    low_range = np.array([0, 120, 80])
    high_range = np.array([5, 255, 255])
    th = cv2.inRange(hsv_img, low_range, high_range)
    dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8)), iterations=2)
    #cv2.imshow('red', dilated)
    #cv2.waitKey(2)

    #dst = cv2.addWeighted(dilated, 0.5, dilated1, 0.5, 0);

    img = cv2.medianBlur(dilated, 5)
    
    
    #th2 = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
  
    circles = [[0,0,0]] 
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=100,param2=10,minRadius=12,maxRadius=40) #10,40
    #circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=80,param2=30,minRadius=10,maxRadius=40) #10,40

    #circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,50,param1=80,param2=30,minRadius=10,maxRadius=50)

    #print (circles)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))  
    else:
        print("cannot get valid value!")
    
    
    #print ("red circles is:",circles)
    
    return circles


def detect_LED_yellow(inImg):

    rects = []
    w = inImg.shape[1]
    h = inImg.shape[0]
    
    if h < 100:
        scale = 2
    else:
        scale = 1

    #cv2.imshow('input', inImg)
    #cv2.waitKey(2)
    
    resizeImg = cv2.resize(inImg, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)

    hsv_img = cv2.cvtColor(resizeImg, cv2.COLOR_BGR2HSV)

    low_range = np.array([15, 100, 70])
    high_range = np.array([40, 255, 255])
    th = cv2.inRange(hsv_img, low_range, high_range)
    dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8)), iterations=2)
    #cv2.imshow('yellow', dilated)
    #cv2.waitKey(2)

    #dst = cv2.addWeighted(dilated, 0.5, dilated1, 0.5, 0);

    img = cv2.medianBlur(dilated, 5)
    
    
    #th2 = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
  
    circles = [[0,0,0]] 
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=100,param2=10,minRadius=12,maxRadius=40) #10,40
    #circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=80,param2=30,minRadius=10,maxRadius=40) #10,40

    #circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,50,param1=80,param2=30,minRadius=10,maxRadius=50)

    #print (circles)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
    else:
        print("cannot get valid value!")
    
    
    #print ("yellow circles is:",circles)
    
    return circles


def detect_spatial_LED(inImg):

    rects = []
    w = inImg.shape[1]
    h = inImg.shape[0]
    
    if h < 100:
        scale = 2
    else:
        scale = 1

    #cv2.imshow('input', inImg)
    #cv2.waitKey(2)
    
    resizeImg = cv2.resize(inImg, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)

    hsv_img = cv2.cvtColor(resizeImg, cv2.COLOR_BGR2HSV)

    low_range = np.array([0, 120, 80])
    high_range = np.array([5, 255, 255])
    th = cv2.inRange(hsv_img, low_range, high_range)
    dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8)), iterations=2)
    #cv2.imshow('red', dilated)
    #cv2.waitKey(2)

    low_range1 = np.array([60, 100, 60])
    high_range1 = np.array([96, 255, 255])
    th1 = cv2.inRange(hsv_img, low_range1, high_range1)
    dilated1 = cv2.dilate(th1, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8)), iterations=2)
    #cv2.imshow('green', dilated1)
    #cv2.waitKey(2)

    dst = cv2.addWeighted(dilated, 0.5, dilated1, 0.5, 0);

    img = cv2.medianBlur(dst, 5)
    
    
    #th2 = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
  
    circles = [[0,0,0]] 
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=100,param2=10,minRadius=12,maxRadius=40) #10,40
    #circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=80,param2=30,minRadius=10,maxRadius=40) #10,40

    #circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,50,param1=80,param2=30,minRadius=10,maxRadius=50)

    #print (circles)
    
    if circles is None:
        print("cannot get valid value!")
        return 
    elif len(circles):#circles.all():
        #print("get valid value")
        if len(circles) >= 1:
            circles = np.uint16(np.around(circles))
                
            
            #img = np.copy(resizeImg)
            #circles = np.uint16(np.around(circles))
            
            '''
            for i in circles[0,:]:
                # draw the outer circle
                
                
                cv2.circle(resizeImg,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(resizeImg,(i[0],i[1]),2,(0,0,255),3)

                
                cv2.rectangle(resizeImg,(i[0]-i[2],i[1]+i[2]),(i[0]+i[2],i[1]-i[2]),(255,0,0),5)
                #circle_result.append(i)
            #print(circle_result)

            cv2.imshow('detected circles',resizeImg)
            '''
    else:
        print("value is empty")
    
    #if circles != None: 
    #if circles :
    
    #print (circles)
    
    return circles

def check_Hsv_LED_green(inImg,circles):
    #if inImg.size == 0:
    #    return
    w = inImg.shape[1]
    h = inImg.shape[0]
    
    if h < 100:
        scale = 2
    else:
        scale = 1
        
    resizeImg = cv2.resize(inImg, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)

    wigth_tmp = resizeImg.shape[1]
    light_imgs = []
    for i in circles[0,:]:
        x = i[0]
        
        y = i[1]
        r = i[2]
        #rect_x = (x - r)
        #rect_y = (y - r)
        #crop_img = resizeImg[rect_y:(y+r),rect_x:(x+r)]
        # for brightness check, only get the value with radius 15
        rect_x = (x - 15)
        rect_y = (y - 15)
        crop_img = resizeImg[rect_y:(y+15),rect_x:(x+15)]
        light_imgs.append(crop_img)
        #cv2.imshow("cropped image", crop_img)
        #cv2.waitKey(2)

    light_colors = []

    for cropimg in light_imgs:
        
        light_color = []
        img_gray = cv2.cvtColor(cropimg, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img_gray, 5)
        ret, img = cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
  
        #cv2.imshow("gray", img)
        #cv2.waitKey(2)

        scalar = cv2.mean(img)

        #print (scalar)
        uscalar = np.uint16(np.around(scalar))

        if uscalar[0] > 120:
            light_color = 1
        else:
            light_color = 0

        light_colors.append(light_color)

    #print (light_colors)
            
    return light_colors

def check_Hsv_LED_red(inImg,circles):
    #if inImg.size == 0:
    #    return
    w = inImg.shape[1]
    h = inImg.shape[0]
    
    if h < 100:
        scale = 2
    else:
        scale = 1
        
    resizeImg = cv2.resize(inImg, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)

    wigth_tmp = resizeImg.shape[1]
    light_imgs = []
    for i in circles[0,:]:
        x = i[0]
        
        y = i[1]
        r = i[2]
        #rect_x = (x - r)
        #rect_y = (y - r)
        #crop_img = resizeImg[rect_y:(y+r),rect_x:(x+r)]
        # for brightness check, only get the value with radius 15
        rect_x = (x - 15)
        rect_y = (y - 15)
        crop_img = resizeImg[rect_y:(y+15),rect_x:(x+15)]
        light_imgs.append(crop_img)
        cv2.imshow("cropped image", crop_img)
        cv2.waitKey(2)

    light_colors = []

    for cropimg in light_imgs:
        
        light_color = []
        img_gray = cv2.cvtColor(cropimg, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img_gray, 5)
        ret, img = cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
  
        #cv2.imshow("gray", img)
        #cv2.waitKey(2)

        scalar = cv2.mean(img)

        #print (scalar)
        uscalar = np.uint16(np.around(scalar))

        if uscalar[0] > 120:
            light_color = 1
        else:
            light_color = 0

        light_colors.append(light_color)

    #print (light_colors)
            
    return light_colors

def check_Hsv_LED_yellow(inImg,circles):
    #if inImg.size == 0:
    #    return
    w = inImg.shape[1]
    h = inImg.shape[0]
    
    if h < 100:
        scale = 2
    else:
        scale = 1
        
    resizeImg = cv2.resize(inImg, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)

    wigth_tmp = resizeImg.shape[1]
    light_imgs = []
    for i in circles[0,:]:
        x = i[0]
        
        y = i[1]
        r = i[2]
        #rect_x = (x - r)
        #rect_y = (y - r)
        #crop_img = resizeImg[rect_y:(y+r),rect_x:(x+r)]
        # for brightness check, only get the value with radius 15
        rect_x = (x - 15)
        rect_y = (y - 15)
        crop_img = resizeImg[rect_y:(y+15),rect_x:(x+15)]
        light_imgs.append(crop_img)
        cv2.imshow("cropped image", crop_img)
        cv2.waitKey(2)

    light_colors = []

    for cropimg in light_imgs:
        
        light_color = []
        img_gray = cv2.cvtColor(cropimg, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img_gray, 5)
        ret, img = cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
  
        #cv2.imshow("gray", img)
        #cv2.waitKey(2)

        scalar = cv2.mean(img)

        #print (scalar)
        uscalar = np.uint16(np.around(scalar))

        if uscalar[0] > 120:
            light_color = 1
        else:
            light_color = 0

        light_colors.append(light_color)

    #print (light_colors)
            
    return light_colors


def check_Hsv_LED(inImg,circles):
    #if inImg.size == 0:
    #    return
    w = inImg.shape[1]
    h = inImg.shape[0]
    
    if h < 100:
        scale = 2
    else:
        scale = 1
        
    resizeImg = cv2.resize(inImg, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)

    wigth_tmp = resizeImg.shape[1]
    light_imgs = []
    for i in circles[0,:]:
        x = i[0]
        
        y = i[1]
        r = i[2]
        #rect_x = (x - r)
        #rect_y = (y - r)
        #crop_img = resizeImg[rect_y:(y+r),rect_x:(x+r)]
        # for brightness check, only get the value with radius 15
        rect_x = (x - 15)
        rect_y = (y - 15)
        crop_img = resizeImg[rect_y:(y+15),rect_x:(x+15)]
        light_imgs.append(crop_img)
        cv2.imshow("cropped image", crop_img)
        cv2.waitKey(2)

    light_colors = []

    for cropimg in light_imgs:
        
        light_color = 0
        img_gray = cv2.cvtColor(cropimg, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img_gray, 5)
        ret, img = cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
  
        #cv2.imshow("gray", img)
        #cv2.waitKey(2)

        scalar = cv2.mean(img)

        #print (scalar)
        uscalar = np.uint16(np.around(scalar))

        if uscalar[0] > 120:
            light_color = 1
        else:
            light_color = 0

        light_colors.append(light_color)

    #print (light_colors)
            
    return light_colors


################Testing####################################        
#src = cv2.imread("D:\\video\\pic\\rgb_r2.png") #rgb_r1.png #rgb_r2 #rgb_r3 #rgb_r4 #rgb_r5 rgb_r6
#only valid for check green and red leds
def detectstatus(src):
    w = src.shape[1]
    h = src.shape[0]
    if h < 100:
        scale = 2
    else:
        scale = 1
        
    resizeImg = cv2.resize(src, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)
    
    light_colors = []
    light_color = []
    circles = [[]]

    # detect green
    circles = detect_LED_green(resizeImg)

    if circles is not None:
        status = check_Hsv_LED(resizeImg,circles)
        if status[0] == 1:
            light_color = [1, "On"]
        else:
            light_color = [1, "Off"]
    else: 
        light_color = [1, 'Err']

    light_colors.append(light_color)

    #detect red
    circles = detect_LED_red(resizeImg)

    if circles is not None:
        status = check_Hsv_LED(resizeImg,circles)
        if status[0] == 1:
            light_color = [0, "On"]
        else:
            light_color = [0, "Off"]
    else: 
        light_color = [0, 'Err']

    light_colors.append(light_color)

    print (light_colors)
    
    return light_colors


def detectsingle(src, type):
    w = src.shape[1]
    h = src.shape[0]
    if h < 100:
        scale = 2
    else:
        scale = 1
        
    resizeImg = cv2.resize(src, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)
    
    color_index = 0
    circles = [[]]
    if type == "GREEN":
        color_index = 1
        circles = detect_LED_green(resizeImg)
    elif type == "YELLOW":
        color_index = 2
        circles = detect_LED_yellow(resizeImg)
    else:
        color_index = 0
        circles = detect_LED_red(resizeImg)

    light_colors = []
    light_color = []
    if circles is not None:
        status = check_Hsv_LED(resizeImg,circles)
        if status[0] == 1:
            light_color = [color_index, "On"]
        else:
            light_color = [color_index, "Off"]
    else: 
        light_color = [color_index, 'Err']

    light_colors.append(light_color)
    print (light_colors)
    
    return light_colors

def test():
    src = cv2.imread("F:\\Pic\\test8.jpg") #
    #lock_gate-1.jpg
    #lock_gate-2.jpg
    #lock_gate-3.jpg
    
    w = src.shape[1]
    h = src.shape[0]
    if h < 100:
        scale = 2
    else:
        scale = 1


    resizeImg = cv2.resize(src, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)

    light_colors = []
    light_color = []
    #result = detect_spatial_LED(resizeImg)
    result = detect_LED_yellow(resizeImg)
    if result is not None:
        status = check_Hsv_LED(resizeImg, result)
        if status[0] == 1:
            light_color = [0, "On"]
        else:
            light_color = [0, "Off"]
    else:
        light_color = [[0,"Err"]]
    #result = detect_Lockgate_Status(resizeImg,draw = False)
    light_colors.append(light_color)
    print (light_colors)

    time.sleep(15)

#test()
#detectstatus()

