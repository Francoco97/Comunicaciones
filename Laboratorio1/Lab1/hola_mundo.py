from PIL import Image
import numpy as np
from skimage import io, color, img_as_ubyte
from skimage.feature import greycomatrix, greycoprops
from sklearn.metrics.cluster import entropy
rgbImg = Image.open("img.jpeg")
#rgbImg = io.imread('img.jpeg')
#grayImg = img_as_ubyte(color.rgb2gray(rgbImg))

distances = [1, 2, 3]
angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
properties = ['energy', 'homogeneity']
'''
glcm = greycomatrix(grayImg, 
                       distances=distances, 
                       angles=angles,
                       symmetric=True,
                       normed=True)

feats = np.hstack([greycoprops(glcm, prop).ravel() for prop in properties])
'''
print(entropy(rgbImg))
