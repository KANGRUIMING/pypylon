# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:15:18 2022

@author: Ruimi
"""

import os
import cv2
from pypylon import genicam
from pypylon import pylon


os.environ["PYLON_CAMEMU"] = "5"


converter = pylon.ImageFormatConverter()
# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

maxCamerasToUse = 5

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

    cameras.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

    # Grab c_countOfImagesToGrab from the cameras.
    while cameras.IsGrabbing():
        grabResult = cameras.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():

            cameraContextValue = grabResult.GetCameraContext()

            # Print the index and the model name of the camera.
            # print("Camera ", cameraContextValue, ": ", cameras[cameraContextValue].GetDeviceInfo().GetModelName())

            # Now, the image data can be processed.
            # Access the image data
            image = converter.Convert(grabResult)
            img = image.GetArray()

            window_name = f'Camera-{cameraContextValue:03}'
            cv2.imshow(window_name, img)
            k = cv2.waitKey(1)
            if k == 27:
                break

except genicam.GenericException as e:
    # Error handling
    print("An exception occurred.", e.GetDescription())
    exitCode = 1