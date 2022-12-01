# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:23:41 2022

@author: Ruimi
"""

import cv2
from pypylon import genicam
from pypylon import pylon
import time
import multiprocessing
import threading
import platform



converter = pylon.ImageFormatConverter()
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

waitTime = 1
numFrames = 10

def save_image(camera1):
    while camera1.IsGrabbing():
        for x in range(numFrames):  
            with camera1.RetrieveResult(5000) as grabResult:
                if grabResult.GrabSucceeded():                
                    print('cam#1_' + str(x))
                    image = converter.Convert(grabResult)
                    img = image.GetArray()
                    cv2.imwrite('cam#1_'+ str(x) + '.png', img)  
            print('waiting for ' + str(waitTime) + ' seconds')   
            time.sleep(waitTime)
        break

def save_image2(camera2):
    while camera2.IsGrabbing():
        for x in range(numFrames):  
            with camera2.RetrieveResult(5000) as grabResult:
                if grabResult.GrabSucceeded():
                    print('cam#2_' + str(x))
                    image = converter.Convert(grabResult)
                    img = image.GetArray()
                    cv2.imwrite('cam#2_' + str(x) + '.png', img)
            print('waiting for ' + str(waitTime) + ' seconds')
            time.sleep(waitTime)
        break
                
if __name__ == '__main__':  
    try:
        tlFactory = pylon.TlFactory.GetInstance()
        devices = tlFactory.EnumerateDevices()
        
        camera1 = pylon.InstantCamera(tlFactory.CreateDevice(devices[0]))
        camera2 = pylon.InstantCamera(tlFactory.CreateDevice(devices[1]))

        camera1.Open()
        camera2.Open()
        
        
        camera1.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        camera2.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

        t1 = threading.Thread(target=save_image, args=(camera1,))
        t2 = threading.Thread(target=save_image2, args=(camera2,))

        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
        
        
    except genicam.GenericException as e:
        # Error handling.
        print("An exception occurred.", e.GetDescription())
