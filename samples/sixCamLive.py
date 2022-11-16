# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:17:47 2022

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
            
def liveView5(camera):
    print("Using device 5", camera.GetDeviceInfo().GetModelName())
    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            cameraContextValue = grabResult.GetCameraContext()
            image = converter.Convert(grabResult)
            img = image.GetArray()
            window_name = 'cam5'
            cv2.imshow(window_name, img)
            k = cv2.waitKey(1)
            if k == 27:
                break
            
def liveView6(camera):
    print("Using device 6", camera.GetDeviceInfo().GetModelName())
    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            cameraContextValue = grabResult.GetCameraContext()
            image = converter.Convert(grabResult)
            img = image.GetArray()
            window_name = 'cam6'
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
        camera5 = pylon.InstantCamera(tlFactory.CreateDevice(devices[4]))
        camera6 = pylon.InstantCamera(tlFactory.CreateDevice(devices[5]))
        camera1.Open()
        camera2.Open()
        camera3.Open()
        camera4.Open()
        camera5.Open()
        camera6.Open()
        camera1.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        camera2.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        camera3.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        camera4.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        camera5.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        camera6.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        
        l1 = threading.Thread(target=liveView1, args = (camera1,))
        l2 = threading.Thread(target=liveView2, args = (camera2,))
        l3 = threading.Thread(target=liveView3, args = (camera3,))
        l4 = threading.Thread(target=liveView4, args = (camera4,))
        l5 = threading.Thread(target=liveView5, args = (camera5,))
        l6 = threading.Thread(target=liveView6, args = (camera6,))
        
        l1.start()
        l2.start()
        l3.start()
        l4.start()
        l5.start()
        l6.start()
        l1.join()
        l2.join()
        l3.join()
        l4.join()
        l5.join()
        l6.join()
        
        print('done')
        '''
        t1 = threading.Thread(target=save_image, args=(camera1,))
        t2 = threading.Thread(target=save_image2, args = (camera2,))
        t1.start()
        t2.start()
        print('Processing')
        t1.join()
        t2.join()
        print('done')
        '''
        
            
    except genicam.GenericException as e:
        # Error handling.
        print("An exception occurred.", e.GetDescription())