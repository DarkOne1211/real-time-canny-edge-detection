import cv2 as cv
import numpy as np 

def real_time_canny(show):
    # VIDEO CAPTURE
    cap_video = cv.VideoCapture(0)

    # RUNS FOREVER
    while(1):
        _,frame = cap_video.read()

        # CANNY EDGE DETECTION 
        edges = cv.Canny(frame,100,200)
        if (show):
            # DISPLAY ORIGINAL
            cv.imshow('Original Image',frame)

            # DISPLAY CANNY OUTPUT
            cv.imshow('Edges',edges)

        cv.waitKey(5)

    cap_video.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    real_time_canny(1)