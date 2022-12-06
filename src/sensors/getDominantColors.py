import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import PIL
from collections import Counter
from sklearn.cluster import KMeans
#%matplotlib inline

def readImage():
    img = cv.imread("batman.png")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    dim = (500, 300)
    # resize image
    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    return img

def saveCoefficients(colors_influence, f):
    f.write("inluence_coefficients:\n")
    for key in colors_influence.keys():
        f.write('%s:%s\n' % (key, colors_influence[key]))

def saveColors(dominant_colors, f):
    f.write("dominant_colors:\n")
    for line in dominant_colors:
        f.write(str(line) + "\n")    

def saveDataToFile(dominant_colors, colors_influence, filename='result.txt'):
    f = open(filename, 'w')
    saveCoefficients(colors_influence, f)
    saveColors(dominant_colors, f)
    f.close()

def palette_perc(k_cluster):
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)
    
    n_pixels = len(k_cluster.labels_)
    counter = Counter(k_cluster.labels_) # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = np.round(counter[i]/n_pixels, 2)
    perc = dict(sorted(perc.items()))
    
    #for logging purposes
    print(perc)
    print(k_cluster.cluster_centers_)
    saveDataToFile(k_cluster.cluster_centers_, perc)
    return(k_cluster.cluster_centers_[0])
    '''
    
    step = 0
    
    for idx, centers in enumerate(k_cluster.cluster_centers_): 
        palette[:, step:int(step + perc[idx]*width+1), :] = centers
        step += int(perc[idx]*width+1)
        
    return palette
    '''

def getDominantColors(img):
    clt = KMeans(n_clusters=5)
    clt_1 = clt.fit(img.reshape(-1, 3))
    palette_perc(clt_1)

'''
img = readImage()
clt = KMeans(n_clusters=5)

clt_1 = clt.fit(img.reshape(-1, 3))
show_img_compar(img, palette_perc(clt_1))
'''
