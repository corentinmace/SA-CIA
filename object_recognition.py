import cv2 as cv
import numpy as np

def searchInImage(haystack):

    capture = haystack
    menu = cv.imread('images/menu.png', cv.IMREAD_UNCHANGED)
    selected_menu = cv.imread('images/selected_menu.png', cv.IMREAD_UNCHANGED)

    capture = cv.cvtColor(capture, cv.COLOR_BGR2GRAY)
    menu = cv.cvtColor(menu, cv.COLOR_BGR2GRAY)
    selected_menu = cv.cvtColor(selected_menu, cv.COLOR_BGR2GRAY)

    menu_w = menu.shape[1]
    menu_h = menu.shape[0]

    selected_menu_w = selected_menu.shape[1]
    selected_menu_h = selected_menu.shape[0]

    result = cv.matchTemplate(capture, menu, cv.TM_CCOEFF_NORMED)
    threshold = 0.4
    locations = np.where(result >= threshold)

    locations = list(zip(*locations[::-1]))

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), menu_w, menu_h]
        rectangles.append(rect)

    rectangles, weigths = cv.groupRectangles(rectangles, 1, 0.3)


    line_color = (0, 0, 255)
    line_type = cv.LINE_4
    font                   = cv.FONT_HERSHEY_PLAIN
    fontScale              = 1.2
    fontColor              = (0, 0, 255)
    thickness              = 2
    lineType               = 2

    for (x, y, w, h) in rectangles:
        top_left = (x, y)
        bottom_right = (x + w, y + h)

        cv.rectangle(haystack, top_left, bottom_right, line_color, line_type)
        cv.putText(haystack ,'MENU', 
        (x+5, y+20), 
        font, 
        fontScale,
        fontColor,
        thickness,
        lineType)

    result = cv.matchTemplate(capture, selected_menu, cv.TM_CCOEFF_NORMED)
    threshold = 0.4
    locations = np.where(result >= threshold)

    locations = list(zip(*locations[::-1]))

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), menu_w, menu_h]
        rectangles.append(rect)

    rectangles, weigths = cv.groupRectangles(rectangles, 1, 0.3)

    line_color = (0, 255, 0)
    fontColor  = (0, 255, 0)

    for (x, y, w, h) in rectangles:
        top_left = (x, y)
        bottom_right = (x + w, y + h)

        cv.rectangle(haystack, top_left, bottom_right, line_color, line_type)
        cv.putText(haystack ,'SELECTED_MENU', 
        (x+5, y+20), 
        font, 
        fontScale,
        fontColor,
        thickness,
        lineType)


    
    return haystack


# def searchInImage(haystack):

#     capture = haystack
#     menu = cv.imread('images/tosearch.png', cv.IMREAD_UNCHANGED)

#     capture = cv.cvtColor(capture, cv.COLOR_BGR2GRAY)
#     tosearch = cv.cvtColor(tosearch, cv.COLOR_BGR2GRAY)

#     result = cv.matchTemplate(capture, tosearch, cv.TM_CCOEFF_NORMED)

#     # Get the best match position
#     min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

#     threshold = 0.5
#     if max_val >= threshold:
#         # print('Needle Found')
#         # print('Location: %s' % str(max_loc))
#         # print('Confidence: %s' % max_val)

#         tosearch_w = tosearch.shape[1]
#         tosearch_h = tosearch.shape[0]

#         top_left = max_loc
#         bottom_right = (top_left[0] + tosearch_w, top_left[1] + tosearch_h)

#         cv.rectangle(haystack, top_left, bottom_right, color=(0, 0, 255), thickness=2, lineType=cv.LINE_4)

#         font                   = cv.FONT_HERSHEY_PLAIN
#         bottomLeftCornerOfText = (top_left[0], top_left[1]-5)
#         fontScale              = 1.2
#         fontColor              = (0, 0, 255)
#         thickness              = 2
#         lineType               = 2

#         cv.putText(haystack ,'VERSUS_MENU', 
#         bottomLeftCornerOfText, 
#         font, 
#         fontScale,
#         fontColor,
#         thickness,
#         lineType)
    
#     return haystack