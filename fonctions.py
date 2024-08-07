import os 
import cv2
import streamlit as st
import numpy as np
from descripteur import glcm,Bitdesc,haralick,glcm_bitdesc,haralick_bitdesc
    

def extract_features(image_path ,descripteur):
    if descripteur=='glcm':
        img=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE) 
        if img is not None:
            features=glcm(img)
            return features
        else:
            pass
    elif descripteur=='bitdesc':
       
        img=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE) 
        if img is not None:
            features=Bitdesc(img)
            return features
        else:
            pass
    elif descripteur=='haralick':
       
        img=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE) 
        if img is not None:
            features=haralick(img)
            return features
        else:
            pass
    elif descripteur=='glcm_bitdesc':
       
        img=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE) 
        if img is not None:
            features=glcm_bitdesc(img)
            return features
        else:
            pass
    elif descripteur=='haralick_bitdesc':
       
        img=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE) 
        if img is not None:
            features=haralick_bitdesc(img)
            return features
        else:
            pass
    