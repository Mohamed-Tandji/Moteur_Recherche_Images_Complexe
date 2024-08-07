# Imports 

#scikit-image
from skimage.feature import graycomatrix,graycoprops

#import biydesc
from BiT import bio_taxo

# Import Haralick
import mahotas.features as features

# Import cv2
import cv2


#pour voir l'implementation on fait ctrl + clique


def glcm(data):
    glcm=graycomatrix(data,[2],[0],1024,symmetric=True,normed=True)
    diss=graycoprops(glcm,'dissimilarity')[0,0]
    con=graycoprops(glcm,'contrast')[0,0]
    corr=graycoprops(glcm,'correlation')[0,0]
    ener=graycoprops(glcm,'energy')[0,0]
    homo=graycoprops(glcm,'homogeneity')[0,0]
    return [diss,con,corr,ener,homo]


def Bitdesc(data):
    return bio_taxo(data)


def haralick(image):
    return features.haralick(image).mean(0).tolist()



def glcm_bitdesc(image):
    return glcm(image)+Bitdesc(image)


def haralick_bitdesc(image):
    return haralick(image)+Bitdesc(image)