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
        
def save_image1(camera):

    
    
    frames_to_grab = 1
    # store last framecount in array
    frame_counts = [0]*1
    frame_counts
    #camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    img = pylon.PylonImage()

    while camera.IsGrabbing():
        with camera.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():
                if grabResult.GrabSucceeded():
                    img_nr = grabResult.ImageNumber
                    cameraContextValue = grabResult.GetCameraContext()
                    frame_counts[cameraContextValue] = img_nr
                    print('cam2' +f"image #{img_nr}")

                    image = converter.Convert(grabResult)
                    img = image.GetArray()
                    cv2.imwrite('cam1' +f"image #{img_nr}" + '.png', img)
                 
                    if min(frame_counts) >= frames_to_grab:
                        print( f"all cameras have acquired {frames_to_grab} frames")
                        break

def save_image2(camera2):
    frames_to_grab = 1
    # store last framecount in array
    frame_counts = [0]*1
    frame_counts
    #camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    img = pylon.PylonImage()
    while camera2.IsGrabbing():
        with camera2.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():
                if grabResult.GrabSucceeded():
                    img_nr = grabResult.ImageNumber
                    cameraContextValue = grabResult.GetCameraContext()
                    frame_counts[cameraContextValue] = img_nr
                    print('cam2' +f"image #{img_nr}")
                    image = converter.Convert(grabResult)
                    img = image.GetArray()
                    cv2.imwrite('cam2' +f"image #{img_nr}" + '.png', img)
                    if min(frame_counts) >= frames_to_grab:
                        print( f"all cameras have acquired {frames_to_grab} frames")
                        break
                    
def save_image3(camera3):
    frames_to_grab = 1
    # store last framecount in array
    frame_counts = [0]*1
    frame_counts
    #camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    img = pylon.PylonImage()
    while camera3.IsGrabbing():
        with camera3.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():
                if grabResult.GrabSucceeded():
                    img_nr = grabResult.ImageNumber
                    cameraContextValue = grabResult.GetCameraContext()
                    frame_counts[cameraContextValue] = img_nr
                    print('cam3' +f"image #{img_nr}")
                    image = converter.Convert(grabResult)
                    img = image.GetArray()
                    cv2.imwrite('cam3' +f"image #{img_nr}" + '.png', img)
                    if min(frame_counts) >= frames_to_grab:
                        print( f"all cameras have acquired {frames_to_grab} frames")
                        break
                    
                    
def save_image4(camera4):
    frames_to_grab = 1
    # store last framecount in array
    frame_counts = [0]*1
    frame_counts
    #camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    img = pylon.PylonImage()
    while camera4.IsGrabbing():
        with camera4.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():
                if grabResult.GrabSucceeded():
                    img_nr = grabResult.ImageNumber
                    cameraContextValue = grabResult.GetCameraContext()
                    frame_counts[cameraContextValue] = img_nr
                    print('cam4' +f"image #{img_nr}")
                    image = converter.Convert(grabResult)
                    img = image.GetArray()
                    cv2.imwrite('cam4' +f"image #{img_nr}" + '.png', img)
                    if min(frame_counts) >= frames_to_grab:
                        print( f"all cameras have acquired {frames_to_grab} frames")
                        break
                    
                    
def save_image5(camera5):
    frames_to_grab = 1
    # store last framecount in array
    frame_counts = [0]*1
    frame_counts
    #camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    img = pylon.PylonImage()
    while camera5.IsGrabbing():
        with camera5.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():
                if grabResult.GrabSucceeded():
                    img_nr = grabResult.ImageNumber
                    cameraContextValue = grabResult.GetCameraContext()
                    frame_counts[cameraContextValue] = img_nr
                    print('cam5' +f"image #{img_nr}")
                    image = converter.Convert(grabResult)
                    img = image.GetArray()
                    cv2.imwrite('cam5' +f"image #{img_nr}" + '.png', img)
                    if min(frame_counts) >= frames_to_grab:
                        print( f"all cameras have acquired {frames_to_grab} frames")
                        break
                    
                    
def save_image6(camera6):
    frames_to_grab = 1
    # store last framecount in array
    frame_counts = [0]*1
    frame_counts
    #camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    img = pylon.PylonImage()
    while camera6.IsGrabbing():
        with camera6.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():
                if grabResult.GrabSucceeded():
                    img_nr = grabResult.ImageNumber
                    cameraContextValue = grabResult.GetCameraContext()
                    frame_counts[cameraContextValue] = img_nr
                    print('cam6' +f"image #{img_nr}")
                    image = converter.Convert(grabResult)
                    img = image.GetArray()
                    cv2.imwrite('cam6' +f"image #{img_nr}" + '.png', img)
                    if min(frame_counts) >= frames_to_grab:
                        print( f"all cameras have acquired {frames_to_grab} frames")
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
        
        t1 = threading.Thread(target=save_image1, args = (camera1,))
        t2 = threading.Thread(target=save_image2, args = (camera2,))
        t3 = threading.Thread(target=save_image3, args = (camera3,))
        t4 = threading.Thread(target=save_image4, args = (camera4,))
        t5 = threading.Thread(target=save_image5, args = (camera5,))
        t6 = threading.Thread(target=save_image6, args = (camera6,))
        
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        
        print('Processing')

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        
        print('done')
    
        
            
    except genicam.GenericException as e:
        # Error handling.
        print("An exception occurred.", e.GetDescription())
