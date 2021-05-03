import datetime                          # for fetching date and time of the system

from PIL import ImageGrab                # for image grabing Pillow will be used done with ImageGrab method
import numpy as np                       # is used to convert the img to an array so the opencv can perform its tasks.
import cv2                               # is used to show the image an works with the image processing things
from win32api import GetSystemMetrics    # To get the system metrics like to fetch the height and width of the system screen from OS


# Geting the Screen Metrics
width = GetSystemMetrics(0)             # GetSystemMetrics if we pass 0 we get the width of the system from  OS
height = GetSystemMetrics(1)            # GetSystemMetrics if we pass 1 we get the width of the system from OS
print("Width and Height of the Screen : {} * {} ".format(width, height))                    # For geting the exact height and width of the screen DYNAMICALLY

# Getting the date and time and developing dynamic file name
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')   # creating an timestamp and getting the current date-time now and converting it inot strftime('%YEAR-%month-%date  %Hour-%MINUTE-%SECOND')
file_name = f'{time_stamp}.mp4'                                         # assigning the timestamp as an file name for the dynamic file name generation
print("Current Time : {} ".format(time_stamp))

# Capturing the Video
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')                                     # Giving four character which can be used for encoding , decoding of the video by cv2
captured_video = cv2.VideoWriter( file_name , fourcc , 20.0 , (width , height))      # Capturing video by cv2.VideoWriter(FILE-NAME , ENCODING-DECODING of the video (fourcc) , FRAME-RATE, ( WIDTH-HEIGHT)   )

# For WEBCAM
webcam = cv2.VideoCapture(0)         # to capture the webcam VALUE 0 for FIRST CAMERA and VALUE 1 if any other additional camera is setup INCREASING


while True:
    img = ImageGrab.grab(bbox=(0,0,width,height))               # for capturing the image
    img_np = np.array(img)                                      # converting the image to an array so opencv2 can work on it.
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)         # changing the image so we can get the exact the color image BGR TO RGB

    _ , frame = webcam.read()                         # To read the webcam and capture it in the frame
    fr_height , fr_width , _ = frame.shape            # To get the height and width of the webcam frame video from FRAME.SHAPE
    img_final[0:fr_height , 0:fr_width , :] = frame[0:fr_height , 0:fr_width , :]       # Assigning the array -- image_final 0:HEIGHT , 0:WIDTH , : ] = assigning  frame which we read from webcam height width
    print(fr_height , fr_width)

    cv2.imshow("Screen Recorder" , img_final)                   # to run or show the image  or video
    #cv2.imshow("WebCam" , frame)                    # To run or show the image or video   [ Shows the webcam frame seprately]
    captured_video.write(img_final)                             # writing the captured image

    if cv2.waitKey(10) == ord('q'):                             # if user is pressing q if stop capturing
        break


