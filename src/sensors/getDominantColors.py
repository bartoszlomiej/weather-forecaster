#import cv2 as cv
#import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as img
import pandas as pd
from scipy.cluster.vq import kmeans
from scipy.cluster.vq import whiten


def getRGBvalues(filename):
    image = img.imread(filename)
    r = []
    g = []
    b = []
    for row in image:
        for temp_r, temp_g, temp_b in row:
            r.append(temp_r)
            g.append(temp_g)
            b.append(temp_b)
    return r, g, b


def getClusterCenters(cluster_centers):
    dominant_colors = []
    for cluster_center in cluster_centers:
        red_scaled, green_scaled, blue_scaled = cluster_center
        dominant_colors.append((red_scaled, green_scaled, blue_scaled))
    return dominant_colors


def getDominantColors(filename):
    r, g, b = getRGBvalues(filename)
    df = pd.DataFrame({'red': r, 'green': g, 'blue': b})
    cluster_centers, _ = kmeans(
        df[['red', 'green', 'blue']].values.astype(float), 3)
    return getClusterCenters(cluster_centers)


# Display colors of cluster centers
#plt.imshow([dominant_colors])
#plt.show()

#exemplary usage:
