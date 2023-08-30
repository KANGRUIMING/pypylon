# Grab_ChunkImage.cpp
# ============================================================================
# Basler cameras provide chunk features: The cameras can generate certain information about each image,
# e.g. frame counters, time stamps, and CRC checksums, that is appended to the image data as data "chunks".
# This sample illustrates how to enable chunk features, how to grab images, and how to process the appended
# data. When the camera is in chunk mode, it transfers data blocks that are partitioned into chunks. The first
# chunk is always the image data. When chunk features are enabled, the image data chunk is followed by chunks
# containing the information generated by the chunk features.
# ============================================================================

from pypylon import pylon
from pypylon import genicam

import sys


# Example of a device specific handler for image events.
class SampleImageEventHandler(pylon.ImageEventHandler):
    def OnImageGrabbed(self, camera, grabResult):
        # The chunk data is attached to the grab result and can be accessed anywhere.

        # Native parameter access:
        # When using the device specific grab results the chunk data can be accessed
        # via the members of the grab result data.
        if genicam.IsReadable(grabResult.ChunkTimestamp):
            print("OnImageGrabbed: TimeStamp (Result) accessed via result member: ", grabResult.ChunkTimestamp.Value)


# Number of images to be grabbed.
countOfImagesToGrab = 5

# The exit code of the sample application.
exitCode = 0

try:
    # Only look for cameras supported by Camera_t
    info = pylon.DeviceInfo()
    info.SetDeviceClass("BaslerUsb")

    # Create an instant camera object with the first found camera device that matches the specified device class.
    camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice(info))
    di = camera.GetDeviceInfo()
    print(di.GetDeviceClass())

    # Print the model name of the camera.
    print("Using device ", camera.GetDeviceInfo().GetModelName())

    # Register an image event handler that accesses the chunk data.
    camera.RegisterImageEventHandler(SampleImageEventHandler(), pylon.RegistrationMode_Append, pylon.Cleanup_Delete)

    # Open the camera.
    camera.Open()

    # A GenICam node map is required for accessing chunk data. That's why a small node map is required for each grab result.
    # Creating a node map can be time consuming, because node maps are created by parsing an XML description file.
    # The node maps are usually created dynamically when StartGrabbing() is called.
    # To avoid a delay caused by node map creation in StartGrabbing() you have the option to create
    # a static pool of node maps once before grabbing.
    camera.StaticChunkNodeMapPoolSize = camera.MaxNumBuffer.GetValue()

    # Enable chunks in general.
    if genicam.IsWritable(camera.ChunkModeActive):
        camera.ChunkModeActive = True
    else:
        raise pylon.RuntimeException("The camera doesn't support chunk features")

    # Enable time stamp chunks.
    camera.ChunkSelector = "Timestamp"
    camera.ChunkEnable = True

    if not camera.IsUsb():
        # Enable frame counter chunks.
        camera.ChunkSelector = "Framecounter"
        camera.ChunkEnable = True

    # Enable CRC checksum chunks.
    camera.ChunkSelector = "PayloadCRC16"
    camera.ChunkEnable = True

    # Start the grabbing of c_countOfImagesToGrab images.
    # The camera device is parameterized with a default configuration which
    # sets up free-running continuous acquisition.
    camera.StartGrabbingMax(countOfImagesToGrab)

    counter = 0
    # Camera.StopGrabbing() is called automatically by the RetrieveResult() method
    # when c_countOfImagesToGrab images have been retrieved.
    while camera.IsGrabbing():
        counter += 1
        print(counter)
        # Wait for an image and then retrieve it. A timeout of 5000 ms is used.
        # RetrieveResult calls the image event handler's OnImageGrabbed method.
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        print("GrabSucceeded: ", grabResult.GrabSucceeded())

        # The result data is automatically filled with received chunk data.
        # (Note:  This is not the case when using the low-level API)
        print("SizeX: ", grabResult.Width)
        print("SizeY: ", grabResult.Height)
        img = grabResult.GetArray()
        print("Gray value of first pixel: ", img[0, 0])

        # Check to see if a buffer containing chunk data has been received.
        if pylon.PayloadType_ChunkData != grabResult.PayloadType:
            raise pylon.RuntimeException("Unexpected payload type received.")

        # Since we have activated the CRC Checksum feature, we can check
        # the integrity of the buffer first.
        # Note: Enabling the CRC Checksum feature is not a prerequisite for using
        # chunks. Chunks can also be handled when the CRC Checksum feature is deactivated.
        if grabResult.HasCRC() and grabResult.CheckCRC() == False:
            raise pylon.RuntimeException("Image was damaged!")

        # Access the chunk data attached to the result.
        # Before accessing the chunk data, you should check to see
        # if the chunk is readable. When it is readable, the buffer
        # contains the requested chunk data.
        if genicam.IsReadable(grabResult.ChunkTimestamp):
            print("TimeStamp (Result): ", grabResult.ChunkTimestamp.Value)

        # USB camera devices provide generic counters. An explicit FrameCounter value is not provided by USB camera devices.
        if not camera.IsUsb():
            if genicam.IsReadable(grabResult.ChunkFramecounter):
                print("FrameCounter (Result): ", grabResult.ChunkFramecounter.Value)
        print()

    # Disable chunk mode.
    camera.ChunkModeActive = False
    camera.Close()

except genicam.GenericException as e:
    # Error handling.
    print("An exception occurred.", e)
    exitCode = 1
