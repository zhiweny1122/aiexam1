# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:09:02 2018

@author: Administrator
"""

import cv2

filename = './aaa.jpg'

def detect(filename):
    face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
    
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.069, 3)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.namedWindow('Viking detected')
    cv2.imshow('Viking detected',img)
    cv2.imwrite('./vikings.jpg',img)
    cv2.waitKey(0)

detect(filename)