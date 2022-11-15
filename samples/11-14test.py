import cv2
import numpy as np
import pypylon
from pypylon import pylon
import time
import os
import multiprocessing


def save_image(camera):
    camera.Open()
    camera.ExposureTime.SetValue(10000)
    camera.Gain.SetValue(0)
    camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    converter = pylon.ImageFormatConverter()
    converter.OutputPixelFormat = pylon.PixelType_BGR8packed
    converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            image = converter.Convert(grabResult)
            img = image.GetArray()
            cv2.imwrite('image.png', img)
            grabResult.Release()
        else:
            print("Error: ", grabResult.ErrorCode, grabResult.ErrorDescription)
    camera.Close()



if __name__ == '__main__':
    from pypylon import pylon
    tlFactory = pylon.TlFactory.GetInstance()
    devices = tlFactory.EnumerateDevices()
    camera = pylon.InstantCamera(tlFactory.CreateDevice(devices[0]))
    camera2 = pylon.InstantCamera(tlFactory.CreateDevice(devices[1]))
    p1 = multiprocessing.Process(target=save_image, args=(camera,))
    p2 = multiprocessing.Process(target=save_image, args=(camera2,))
        
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    pypylon.pylon_terminate()
