#import cv2 as cv
#import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as img
import pandas as pd
from scipy.cluster.vq import kmeans
from scipy.cluster.vq import whiten
#%matplotlib inline
'''
def readImage():
    img = cv.imread("batman.png")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    dim = (500, 300)
    # resize image
    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    return img

#image = readImage()
'''

def getRGBvalues(filename):
    image = img.imread(filename)
    r = []
    g = []
    b = []
    for row in image:
        for temp_r, temp_g, temp_b, temp in row:
            r.append(temp_r)
            g.append(temp_g)
            b.append(temp_b)
    return r, g, b

def getDominantColors(r, g, b):
    batman_df = pd.DataFrame({'red' : r,'green' : g,'blue' : b})
    cluster_centers, _ = kmeans(batman_df[['red','green','blue']].values.astype(float), 3)
    dominant_colors = []

    for cluster_center in cluster_centers:
        red_scaled, green_scaled, blue_scaled = cluster_center
        dominant_colors.append((red_scaled,
	                        green_scaled,
	                        blue_scaled))
    return dominant_colors

# Display colors of cluster centers
#plt.imshow([dominant_colors])
#plt.show()

#exemplary usage:
r, g, b = getRGBvalues("batman.png")
print(getDominantColors(r, g, b))
