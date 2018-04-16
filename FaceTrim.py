# coding: utf-8

import os
import glob
import re
import cv2
import numpy as np

def FaceDetect(img):
    face_cascade = cv2.CascadeClassifier('lbpcascade_animeface.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    
    return faces


def RenameFiles(path, extension):
    image_dir = glob.glob(path + '/*')
    
    for i, file_name in enumerate(image_dir):
        image_path = path + str(i) + extension
        if os.path.exists(image_path):
            continue
        else:
            os.rename(file_name, os.path.join(path, str(i) + extension))


def TrimFaces(images_path, faces_path, extension):
    images = os.listdir(images_path)
    count = 0
    for image in images:
        index = re.search(extension, image)
        if index:
            count = count + 1

    for i in range(count):
        image = cv2.imread(images_path + '/' + str(i) + extension)
        faces = facedetect(images)

        if not os.path.exists(faces_path):
            os.makedirs(output_dir)

        for j, (x,y,w,h) in enumerate(faces):
            face_image = image[y:y+h, x:x+w]
            faces_path = os.path.join(faces_path, '/' + str(i) + '_' + str(j) + extension)
            cv2.imwrite(faces_path, face_image)


if __name__ == '__main__':
    images_path = './images'
    faces_path = './faces'
    extension = '.png'
    
    RenameFiles(images_path, extension)
    TrimFaces(images_path, faces_path, extension)

    
