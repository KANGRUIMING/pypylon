
import os
import cv2
import numpy as np
from pypylon import genicam
from pypylon import pylon
import keyboard
import time
import threading

os.environ["PYLON_CAMEMU"] = "5"


converter = pylon.ImageFormatConverter()
# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

maxCamerasToUse = 2

# The exit code of the sample application.
exitCode = 0

try:
    
    # Get the transport layer factory.
    tlFactory = pylon.TlFactory.GetInstance()

    # Get all attached devices and exit application if no device is found.
    devices = tlFactory.EnumerateDevices()
    if len(devices) == 0:
        raise pylon.RuntimeException("No camera present.")

    # Create an array of instant cameras for the found devices and avoid exceeding a maximum number of devices.
    cameras = pylon.InstantCameraArray(min(len(devices), maxCamerasToUse))

    # Create and attach all Pylon Devices.
    for idx, cam in enumerate(cameras):
        cam.Attach(tlFactory.CreateDevice(devices[idx]))
        print("Using device ", cam.GetDeviceInfo().GetModelName())
        
        # setup named window per camera
        window_name = f'Camera-{idx:03}'
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        
        
    
    frames_to_grab = 1
    # store last framecount in array
    frame_counts = [0]*maxCamerasToUse
    frame_counts


    cameras.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    


    # Grab c_countOfImagesToGrab from the cameras.
    while cameras.IsGrabbing():
        #grabResult = cameras.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        with cameras.RetrieveResult(500) as grabResult:
            if grabResult.GrabSucceeded():
                img_nr = grabResult.ImageNumber
                cameraContextValue = grabResult.GetCameraContext()
                frame_counts[cameraContextValue] = img_nr
                print(f"cam #{cameraContextValue}  image #{img_nr}")
    
                # Print the index and the model name of the camera.
                # print("Camera ", cameraContextValue, ": ", cameras[cameraContextValue].GetDeviceInfo().GetModelName())
    
                # Now, the image data can be processed.
                # Access the image data
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite(f"cam#{cameraContextValue}image #{img_nr}" + '.png', img)
                
               # x = len(img)
                #print (x)
                #img1 = np.array(img, dtype=np.uint8)
                
               
                window_name = f'Camera-{cameraContextValue:03}'
                #cv2.imshow(window_name, img)
    
               # if keyboard.is_pressed('p'):
                    #cv2.imwrite('Cam1' +  '.png', img1)
                    #cv2.imwrite('Cam2' +  '.png', img1[1])pp
                if min(frame_counts) >= frames_to_grab:
                    print( f"all cameras have acquired {frames_to_grab} frames")
                    break
                
                k = cv2.waitKey(1)
                if k == 27:
                    break

except genicam.GenericException as e:
    # Error handling
    print("An exception occurred.", e.GetDescription())
