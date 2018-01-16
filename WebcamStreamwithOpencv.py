"""
Exercise2 : Solution

"""
import cv2
import numpy as np
import matplotlib
import time
import itertools


def display_images():
    """
    This function obtains results from generators and plot image and image intensity
    """
    vc = cv2.VideoCapture(0)  # Open webcam using opencv 0 = First available camera
    cv2.namedWindow('image', 0)  # 0 enables resizing the window as seen in next line

    fps = vc.get(cv2.CAP_PROP_FPS)
    print('Frames per second is {:0.2f}'.format(fps))
    count = 0
    starttime = time.time()

    # Collect a single image
    previmage = next(stream_frames(vc))
    while vc.isOpened():
        for nextimage in stream_frames(vc):
            # i[0] : bgr image
            # You can chuck the matplotlib plotting tools
            cv2.imshow('image', cv2.absdiff(previmage, nextimage))  # Plot image
            previmage = nextimage
            count += 1

        # Get out on keypress
        keypress = cv2.waitKey(1)
        if keypress == ord('q'):
            elapsedtime = time.time() - starttime
            print('The collection FPS was {:0.2f}'.format(count / elapsedtime))
            vc.release()
            cv2.destroyAllWindows()
            break


def stream_frames(video_capture):
    """
    This generator function acquires images, convert to rgb, get mean intensity
    and yield necessary results
    :param  video_capture: the video capture object from opencv
    :yield  BGR_image
            Image Intensity
    """
    # Opencv uses BGR, so no need to convert here
    _, frame = video_capture.read()  # Read image from webcam
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # Resize image by half to fit display
    intensity = np.mean(frame)  # Get mean intensity
    yield frame


display_images()
