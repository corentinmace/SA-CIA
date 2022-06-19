import cv2 as cv
import numpy as np

#capture = cv.imread('images/capture.png', cv.IMREAD_UNCHANGED)
def searchInImage(haystack):

    capture = haystack
    tosearch = cv.imread('images/tosearch.png', cv.IMREAD_UNCHANGED)

    capture = cv.cvtColor(capture, cv.COLOR_BGR2GRAY)
    tosearch = cv.cvtColor(tosearch, cv.COLOR_BGR2GRAY)

    result = cv.matchTemplate(capture, tosearch, cv.TM_CCOEFF_NORMED)

    # Get the best match position
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)


    threshold = 0.8
    if max_val >= threshold:
        # print('Needle Found')
        # print('Location: %s' % str(max_loc))
        # print('Confidence: %s' % max_val)

        tosearch_w = tosearch.shape[1]
        tosearch_h = tosearch.shape[0]

        top_left = max_loc
        bottom_right = (top_left[0] + tosearch_w, top_left[1] + tosearch_h)

        cv.rectangle(haystack, top_left, bottom_right, color=(0, 0, 255), thickness=2, lineType=cv.LINE_4)

        font                   = cv.FONT_HERSHEY_PLAIN
        bottomLeftCornerOfText = (top_left[0], top_left[1]-5)
        fontScale              = 1.2
        fontColor              = (0, 0, 255)
        thickness              = 2
        lineType               = 2

        cv.putText(haystack ,'VERSUS_MENU', 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        thickness,
        lineType)
    
    return haystack