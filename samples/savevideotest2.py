# Import the necessary modules
import cv2
import numpy as np
from pypylon import genicam
from pypylon import pylon
import time
import multiprocessing
import threading
import platform
from numba import jit
# Create an ImageFormatConverter object to convert the image format to a format that can be saved using OpenCV


# Set the number of frames to be captured and the waiting time between frames
# Define the function that will be used to record video from the first camera
def save_video(camera1):
    # Create a VideoWriter object for the first camera
    x=0
    # Start the timer
    start_time = time.time()
    while camera1.IsGrabbing():
        # Grab a frame from the camera
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():
                # Convert the frame to a format that can be saved using OpenCV
                image = converter.Convert(grabResult)
                img = image.GetArray()
                print('cam#1_' + str(x))
                cv2.imwrite('cam1_' + str(x)+ '.jpeg', img)
                x += 1
                # Calculate the elapsed time
                elapsed_time = time.time() - start_time
                # If the elapsed time is greater than or equal to 10 seconds, break the loop
                if elapsed_time >= 1:
                    break
   
def save_video2(camera2):
    
    # Create a VideoWriter object for the first camera
    x=0
    # Start the timer
    start_time = time.time()
    while camera2.IsGrabbing():
        # Grab a frame from the camera
        with camera2.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():

                # Convert the frame to a format that can be saved using OpenCV
                image = converter.Convert(grabResult)
                img = image.GetArray()
                print('cam#2_' + str(x))
                cv2.imwrite('cam2_' + str(x) + '.jpeg', img)
                x += 1  
                # Calculate the elapsed time
                elapsed_time = time.time() - start_time
                # If the elapsed time is greater than or equal to 10 seconds, break the loop
                if elapsed_time >= 1:
                    break
    
    
    
    
if __name__ == '__main__':  
    try:
        # Enumerate the available cameras and create InstantCamera objects for each one
        tlFactory = pylon.TlFactory.GetInstance()
        devices = np.array(tlFactory.EnumerateDevices())

        camera1 = pylon.InstantCamera(tlFactory.CreateDevice(devices[0]))
        camera2 = pylon.InstantCamera(tlFactory.CreateDevice(devices[1]))
        
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        


        camera1.Open()
        camera2.Open()

        # Start grabbing frames from the cameras in a separate thread for each camera
        camera1.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        camera2.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

        t1 = threading.Thread(target=save_video, args=(camera1,))
        t2 = threading.Thread(target=save_video2, args=(camera2,))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

    except genicam.GenericException as e:
        # Error handling
        print("An exception occurred.", e.GetDescription())