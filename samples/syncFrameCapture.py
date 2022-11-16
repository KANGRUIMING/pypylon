import cv2
from pypylon import genicam
from pypylon import pylon
import time
import multiprocessing
import threading
import platform


  
    
#def live(camera):
   # for cam in enumerate(devices):
       # cam.Attach(camera)
       # print("Using device ", cam.GetDeviceInfo().GetModelName())
       # # setup named window per camera
      #  window_name = f'Camera-{cam:03}'
      #  cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)


        
def save_image(camera):

    converter = pylon.ImageFormatConverter()
    converter.OutputPixelFormat = pylon.PixelType_BGR8packed
    converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
    
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
                    print(f"cam #{cameraContextValue}  image #{img_nr}")

                    image = converter.Convert(grabResult)
                    img = image.GetArray()
                    cv2.imwrite(f"cam#{cameraContextValue}image #{img_nr}" + '.png', img)
                 
                    if min(frame_counts) >= frames_to_grab:
                        print( f"all cameras have acquired {frames_to_grab} frames")
                        break

def save_image2(camerax):

    converter = pylon.ImageFormatConverter()
    converter.OutputPixelFormat = pylon.PixelType_BGR8packed
    converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
    
    frames_to_grab = 1
    # store last framecount in array
    frame_counts = [0]*1
    frame_counts
    #camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    img = pylon.PylonImage()

    while camerax.IsGrabbing():
        with camerax.RetrieveResult(5000) as grabResult:
            if grabResult.GrabSucceeded():
                if grabResult.GrabSucceeded():
                    img_nr = grabResult.ImageNumber
                    cameraContextValue = grabResult.GetCameraContext()
                    frame_counts[cameraContextValue] = img_nr
                    print(f"cam #{cameraContextValue}  image #{img_nr}")

                    image = converter.Convert(grabResult)
                    img = image.GetArray()
                    cv2.imwrite(f"cam#{cameraContextValue}image #{img_nr}camx" + '.png', img)
                 
                    if min(frame_counts) >= frames_to_grab:
                        print( f"all cameras have acquired {frames_to_grab} frames")
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
        t2 = threading.Thread(target=save_image2, args = (camera2,))
        t1.start()
        t2.start()
        print('Processing')
        t1.join()
        t2.join()
        print('done')
    
        
            
    except genicam.GenericException as e:
        # Error handling.
        print("An exception occurred.", e.GetDescription())
