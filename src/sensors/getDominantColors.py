import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import PIL
from collections import Counter
#from sklearn.cluster import KMeans
import pandas as pd
from scipy.cluster.vq import kmeans
from scipy.cluster.vq import whiten
#%matplotlib inline

def readImage():
    img = cv.imread("batman.png")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    dim = (500, 300)
    # resize image
    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    return img

#image = readImage()

# Import image class of matplotlib
import matplotlib.image as img

# Read batman image and print dimensions
image = img.imread('batman.png')
print(image.shape)

# Store RGB values of all pixels in lists r, g and b
r = []
g = []
b = []
for row in image:
    for temp_r, temp_g, temp_b, temp in row:
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

# Saving as DataFrame
batman_df = pd.DataFrame({'red' : r,'green' : g,'blue' : b})

# Scaling the values
batman_df['scaled_color_red'] = whiten(batman_df['red'])
batman_df['scaled_color_blue'] = whiten(batman_df['blue'])
batman_df['scaled_color_green'] = whiten(batman_df['green'])


cluster_centers, _ = kmeans(batman_df[['scaled_color_red','scaled_color_blue','scaled_color_green']], 3)

dominant_colors = []

# Get standard deviations of each color
red_std, green_std, blue_std = batman_df[['red','green','blue']].std()

for cluster_center in cluster_centers:
    red_scaled, green_scaled, blue_scaled = cluster_center
    # Convert each standardized value to scaled value
    dominant_colors.append((red_scaled * red_std / 255,
	                    green_scaled * green_std / 255,
	                    blue_scaled * blue_std / 255
                            ))

# Display colors of cluster centers
plt.imshow([dominant_colors])
plt.show()

print(dominant_colors)

'''

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
'''
    step = 0
    
    for idx, centers in enumerate(k_cluster.cluster_centers_): 
        palette[:, step:int(step + perc[idx]*width+1), :] = centers
        step += int(perc[idx]*width+1)
        
    return palette
'''
'''
def getDominantColors(img):
    clt = KMeans(n_clusters=5)
    clt_1 = clt.fit(img.reshape(-1, 3))
    palette_perc(clt_1)
'''
'''
img = readImage()
clt = KMeans(n_clusters=5)

clt_1 = clt.fit(img.reshape(-1, 3))
show_img_compar(img, palette_perc(clt_1))
'''
