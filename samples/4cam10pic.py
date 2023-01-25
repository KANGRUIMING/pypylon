# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:51:16 2022

@author: Ruimi
"""

import cv2
from pypylon import genicam
from pypylon import pylon
import time
import multiprocessing
import threading
import platform


def getkey():
    return input("Enter \"t\" to trigger the camera: ")

converter = pylon.ImageFormatConverter()
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

waitTime = 1
        
def save_image(camera1):
    while camera1.IsGrabbing():
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#1 img#1')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#1_1'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#1 img#2')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#1_2'+ '.png', img)
        
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#1 img#3')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#1_3'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#1 img#4')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#1_4'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#1 img#5')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#1_5'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#1 img#6')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#1_6'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#1 img#7')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#1_7'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#1 img#8')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#1_8'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#1 img#9')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#1_9'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#1 img#10')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#1_10'+ '.png', img)
            
                break

def save_image2(camera2):
    while camera2.IsGrabbing():
        with camera2.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():
                print('cam#2 img#1')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#2_1' + '.png', img)
        print('waiting for ' + str(waitTime) + ' seconds')
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#2 img#2')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#2_2'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#2 img#3')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#2_3'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#2 img#4')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#2_4'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#2 img#5')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#2_5'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#2 img#6')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#2_6'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#2 img#7')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#2_7'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#2 img#8')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#2_8'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#2 img#9')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#2_9'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#2 img#10')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#2_10'+ '.png', img)
                
                break

def save_image3(camera3):
    while camera1.IsGrabbing():
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#3 img#1')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#3_1'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#3 img#2')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#3_2'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#3 img#3')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#3_3'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#3 img#4')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#3_4'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#3 img#5')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#3_5'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#3 img#6')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#3_6'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#3 img#7')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#3_7'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#3 img#8')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#3_8'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#3 img#9')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#3_9'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#3 img#10')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#3_10'+ '.png', img)
            
                break

def save_image4(camera4):
    while camera2.IsGrabbing():
        with camera2.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():
                print('cam#4 img#1')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#4_1' + '.png', img)
        print('waiting for ' + str(waitTime) + ' seconds')
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#4 img#2')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#4_2'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#4 img#3')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#4_3'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#4 img#4')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#4_4'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#4 img#5')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#4_5'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#4 img#6')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#4_6'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#4 img#7')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#4_7'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#4 img#8')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#4_8'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#4 img#9')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#4_9'+ '.png', img)
                
        print('waiting for ' + str(waitTime) + ' seconds')   
        time.sleep(waitTime)
        with camera1.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():                
                print('cam#4 img#10')
                image = converter.Convert(grabResult)
                img = image.GetArray()
                cv2.imwrite('cam#4_10'+ '.png', img)
                
                break
            
def liveView1(camera):
    print("Using device 1", camera.GetDeviceInfo().GetModelName())
    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            cameraContextValue = grabResult.GetCameraContext()
            image = converter.Convert(grabResult)
            img = image.GetArray()
            window_name = 'cam1'
            cv2.imshow(window_name, img)
            k = cv2.waitKey(1)
            if k == 27:
                break
            
def liveView2(camera):
    print("Using device 2", camera.GetDeviceInfo().GetModelName())
    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            cameraContextValue = grabResult.GetCameraContext()
            image = converter.Convert(grabResult)
            img = image.GetArray()
            window_name = 'cam2'
            cv2.imshow(window_name, img)
            k = cv2.waitKey(1)
            if k == 27:
                break
            
def liveView3(camera):
    print("Using device 3", camera.GetDeviceInfo().GetModelName())
    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            cameraContextValue = grabResult.GetCameraContext()
            image = converter.Convert(grabResult)
            img = image.GetArray()
            window_name = 'cam3'
            cv2.imshow(window_name, img)
            k = cv2.waitKey(1)
            if k == 27:
                break
            
def liveView4(camera):
    print("Using device 4", camera.GetDeviceInfo().GetModelName())
    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            cameraContextValue = grabResult.GetCameraContext()
            image = converter.Convert(grabResult)
            img = image.GetArray()
            window_name = 'cam4'
            cv2.imshow(window_name, img)
            k = cv2.waitKey(1)
            if k == 27:
                break

if __name__ == '__main__':  
    try:
        tlFactory = pylon.TlFactory.GetInstance()
        devices = tlFactory.EnumerateDevices()
        camera1 = pylon.InstantCamera(tlFactory.CreateDevice(devices[0]))
        camera2 = pylon.InstantCamera(tlFactory.CreateDevice(devices[1]))
        camera3 = pylon.InstantCamera(tlFactory.CreateDevice(devices[2]))
        camera4 = pylon.InstantCamera(tlFactory.CreateDevice(devices[3]))
        camera1.Open()
        camera2.Open()
        camera3.Open()
        camera4.Open()
        camera1.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        camera2.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        camera3.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        camera4.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        t1 = threading.Thread(target=save_image, args=(camera1,))
        t2 = threading.Thread(target=save_image2, args = (camera2,))
        t3 = threading.Thread(target=save_image3, args=(camera3,))
        t4 = threading.Thread(target=save_image4, args = (camera4,))
        
        l1 = threading.Thread(target=liveView1, args = (camera1,))
        l2 = threading.Thread(target=liveView2, args = (camera2,))
        l3 = threading.Thread(target=liveView3, args = (camera3,))
        l4 = threading.Thread(target=liveView4, args = (camera4,))
        
        
        l1.start()
        l2.start()
        l3.start()
        l4.start()
        l1.join()
        l2.join()
        l3.join()
        l4.join()
        
        
        key = getkey()
        print(key)
        if (key == 't' or key == 'T'):
            t1.start()
            t2.start()
            print('Processing')
            t1.join()
            t2.join()
            print('done')
    
        
            
    except genicam.GenericException as e:
        # Error handling.
        print("An exception occurred.", e.GetDescription())
