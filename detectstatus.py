import numpy as np
import cv2


def detect_spatial_LED(inImg):

    rects = []
    w = inImg.shape[1]
    h = inImg.shape[0]
    
    if w > 640 or h > 480:
        scale = 640 / w
    elif w < 320 or h < 240:
        scale = 320 / w
    else: scale = 1

    
    resizeImg = cv2.resize(inImg, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)
    

    if resizeImg.shape[2] == 3:
        gray_img = cv2.cvtColor(resizeImg, cv2.COLOR_BGR2GRAY)
    else:
        gray_img = np.copy(resizeImg)
    
    
    img = cv2.medianBlur(gray_img, 5)
    th2 = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
  
    circles = [[0,0,0]] 
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=80,param2=30,minRadius=10,maxRadius=40) #10,40

    #circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=80,param2=30,minRadius=10,maxRadius=50)

    if circles is None:
        print("cannot get valid value!")
        return 
    elif circles.all():
        print("get valid value")
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
        
    
    return circles
def check_Hsv_LED(inImg,circles):
    #if inImg.size == 0:
    #    return
    w = inImg.shape[1]
    h = inImg.shape[0]
    
    if w > 640 or h > 480:
        scale = 640 / w
    elif w < 320 or h < 240:
        scale = 320 / w
    else:
        scale = 1
        
    resizeImg = cv2.resize(inImg, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)

    wigth_tmp = resizeImg.shape[1]
    light_imgs = []
    for i in circles[0,:]:
        x = i[0]
        
        if x >= 0.5 * wigth_tmp:
            continue
        else:
            y = i[1]
            r = i[2]
            rect_x = (x - r)
            rect_y = (y - r)
            crop_img = resizeImg[rect_y:(y+r),rect_x:(x+r)]
            light_imgs.append(crop_img)

    light_colors = []

    light_ID = 0
    for cropimg in light_imgs:
        
        light_color = []
        img_hsv = cv2.cvtColor(cropimg, cv2.COLOR_BGR2HSV)
  

        
        lower_hsv_G = np.array([60, 0, 220],dtype=np.uint8) #green
        upper_hsv_G = np.array([255, 255, 255],dtype=np.uint8)

        mask_G = cv2.inRange(img_hsv,lower_hsv_G,upper_hsv_G)
    
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

        dilate_mask_G = cv2.dilate(mask_G, kernel)

        
        

        
        lower_hsv_R = np.array([0, 0, 220],dtype=np.uint8) #green
        upper_hsv_R = np.array([50, 255, 255],dtype=np.uint8)

        mask_R = cv2.inRange(img_hsv,lower_hsv_R,upper_hsv_R)
       
        dilate_mask_R = cv2.dilate(mask_R, kernel)

        area_R = np.count_nonzero(dilate_mask_R)
        area_G = np.count_nonzero(dilate_mask_G)
        
        #print ("area_G,area_R = ",area_G,area_R)

        if area_G > area_R and area_G> 500:
            light_color = "G"
        elif area_G < area_R and area_R > 500 :
            light_color = "R"
        else:
            light_color = "N"

        light_colors.append([light_ID,light_color])
        light_ID += 1
            
    #print("light_colors: ",light_colors)
    return light_colors
    
################Testing####################################        
#src = cv2.imread("D:\\video\\pic\\rgb_r2.png") #rgb_r1.png #rgb_r2 #rgb_r3 #rgb_r4 #rgb_r5 rgb_r6

def detectstatus(src):
    w = src.shape[1]
    h = src.shape[0]
    if w < 320 or h < 240:
        scale = 320 / w
    else:
        scale = 1
        
    resizeImg = cv2.resize(src, (int(scale * w), int(scale* h)), interpolation=cv2.INTER_CUBIC)
    
    circles = [[]]
    circles = detect_spatial_LED(resizeImg)

    if circles is None:
        #print("cannot get valid value!")
        light_colors = [[0, 'E'], [1, 'E']]
    elif circles.all():
        light_colors = check_Hsv_LED(resizeImg,circles)
        #print(light_colors) #[[0, 'R']]  or [[0, 'R'], [1, 'N']]   
    else:
        light_colors = [[0, 'E'], [1, 'E']]

    print(light_colors)
    
    return light_colors

