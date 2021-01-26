import cv2
import numpy as np

class ImageSegmentation():

    @staticmethod
    def region_growing(thresh, dilationKernel, closingKernel):
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, dilationKernel, 7)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, closingKernel)
        dilation = cv2.dilate(thresh, dilationKernel, 3)
        
        return dilation, closing, opening

    @staticmethod
    def distance_transform(opening, dilation, factor=0.7):
        dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
        ret, fg = cv2.threshold(dist_transform, factor*dist_transform.max(), 255, 0)
        fg = np.uint8(fg)
        unknown = cv2.subtract(dilation, fg)
        
        return unknown, fg

    @staticmethod
    def connected_components(fg, unknown):
        ret, markers = cv2.connectedComponents(unknown)
        markers = markers.astype(np.float32)/np.max(markers)
        markers = (markers*255).astype(np.uint8)
        contours, hierarchy = cv2.findContours(markers, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
        return markers, contours

    @staticmethod
    def markers_dilation(markers):
        dilationKernel = np.ones((13,13), np.uint8)
        opening = cv2.morphologyEx(markers, cv2.MORPH_OPEN, dilationKernel, 13)
        dilation = cv2.dilate(opening, dilationKernel, 13)
        
        return dilation

    @staticmethod
    def fit_line(contours, img, color=(0,255,0)):
        rows,cols = img.shape[:2]
        cnt = contours[0]
        [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
        lefty = int((-x*vy/vx) + y)
        righty = int(((cols-x)*vy/vx)+y)
        angle = np.abs(np.arctan((lefty-righty)/(0-(cols-1))))
        angle = min([angle, np.pi/2 - angle]) * 180 / np.pi
        
        return img, angle