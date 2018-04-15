# coding: utf-8

import os
import glob
import re
import cv2
import numpy as np

def facedetect(img):
    face_cascade = cv2.CascadeClassifier('lbpcascade_animeface.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    
    return faces


if __name__ == '__main__':
    # ファイル名を連番にする
    path = "./images"
    files = glob.glob(path + '/*')
    
    for i, f in enumerate(files):
        image_path = path + str(i) + '.png'
        if os.path.exists(image_path):
            continue
        else:
            os.rename(f, os.path.join(path, str(i) + '.png'))
            
    files = os.listdir('./images')
    count = 0
    for file in files:
        index = re.search('.png', file)
        if index:
            count = count + 1

    for i in range(count):
        img = cv2.imread('./images/' + str(i) + '.png')
        faces = facedetect(img)

        output_dir = 'faces/'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for j, (x,y,w,h) in enumerate(faces):
            face_image = img[y:y+h, x:x+w]
            output_path = os.path.join(output_dir, str(i) + '_' + str(j) + '.png')
            cv2.imwrite(output_path,face_image)

