# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 20:05:00 2022

@author: Ruimi
"""

import os
from pypylon import pylon
from multiprocessing import Proces, Value, Array
from pypylon import genicam
import cv2
import numpy as np
import multiprocessing


result_a = []
result_b = []

class CamProcess(Process):
    def __init__(self, queue):
        Process.__init__(self)
        self.data_queue = queue
        self.flag = True
        self.id = None
        self.cam = None

    def run(self):
        if self.id is None:
            self.id = os.getpid()
        self.cam = Basler(flag=0)
        while self.flag:
            ret, frame = self.cam.read()
            if ret:
                self.data_queue.put([self.id, frame])

            else:
                self.data_queue.put(None)

    def stop(self):
        self.flag = False
        self.cam.stop()

maxCamerasToUse = 2

class Basler:
    def __init__(self, flag=0, exposure=None):
        #self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        
        tlFactory = pylon.TlFactory.GetInstance()
        devices = tlFactory.EnumerateDevices()
        self.camera = pylon.InstantCamera(tlFactory.CreateDevice(devices[0]))
        self.camera2 = pylon.InstantCamera(tlFactory.CreateDevice(devices[1]))
            

        # Grabing Continously (video) with minimal delay
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        self.camera2.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

        self.converter = pylon.ImageFormatConverter()

        # converting to opencv bgr format
        self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

        """
        The code below works and it is similar to the code wrapper in 
        "read" function. Calling that function gives error
        """

        # self.some =self.camera.RetrieveResult (5000, pylon.TimeoutHandling_ThrowException)
        # self.image=self.converter.Convert (self.some)
        # self.img=self.image.GetArray ()
        # print(self.img)

    def read(self):
        grab_result = self.camera.RetrieveResult(10000, pylon.TimeoutHandling_ThrowException)
        grab_result2 = self.camera2.RetrieveResult(10000, pylon.TimeoutHandling_ThrowException)
        
        if grab_result.GrabSucceeded():
            # Access the image data
            
            image1 = self.converter.Convert(grab_result)
            image2 = self.converter.Convert(grab_result)

            img1 = image1.GetArray()
            img2 = image2.GetArray()
            

            return True, img1, img2
        else:
            return False, None

    def release(self):
        self.camera.StopGrabbing()
        del self.camera


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=CamProcess, args=(img1)
    p2 = multiprocessing.Process(target=CamProcess, args=(img2))
    p1 = multiprocessing.Process(target=save_image, args=(camera,))
    p2 = multiprocessing.Process(target=save_image, args=(camera2,))
    
    
    processes = []
    num_processers = os.cup_count()
    for i in range(num_processers):
        process = Process(target = Basler)
        processes.append(process)
        
    for process in processes:
        process.start()
        
    for process in processes:
        process.join()
        
    from multiprocessing import Queue
    
    im_q = Queue(maxsize=1)
    cam = CamProcess(im_q)
    cam.start()
    while True:
        data = im_q.get()
        print(data)
