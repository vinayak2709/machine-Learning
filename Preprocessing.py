import imutils
import numpy as np
import cv2

image=cv2.imread('22.png')

t=cv2.fastNlMeansDenoisingColored(image,None,10,10,7,15)                      #denoising color image
cv2.imshow('denoising',t)


gray = cv2.cvtColor(t, cv2.COLOR_BGR2GRAY)                                    # Color to gray

cv2.imshow('Gray',gray)

gausBlr = cv2.GaussianBlur(gray, (5, 5), 0)                                    #gaussian blurring (high pass filtering)


cv2.imshow('GuassianBlur',gausBlr)

thresh = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY)[1]                     #threshorlding according to req

cv2.imshow('Thresholding',thresh)
thresh = cv2.erode(thresh, None, iterations=8)              # errodes fornts width ,   iterations can be changed according to use detection requirements

cv2.imshow('errosion',thresh)


thresh = cv2.dilate(thresh, None, iterations=8)             #enlarges width of fornts

cv2.imshow('dialation',thresh)

cv2.waitKey(0)





