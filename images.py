# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 13:36:49 2016

@author: laco3
@title : Formation Python SISEO 01-02-2016
"""

import numpy as np
import matplotlib.pyplot as plt
import PIL # Biblio pour traitement images
from matplotlib import cm

#path = "D:\Documents\THESE\1ereAnnee\Formations\Python\images\woofy.jpg" # chemin absolu
path = "images\multicolor.jpg" # Chemin relatif dans dossier de travail
im = PIL.Image.open(path)
R, G, B = im.split() # R = rouge, G = vert, B = bleu
R = np.asarray(R, dtype = np.uint8)
G = np.asarray(G, dtype = np.uint8)
B = np.asarray(B, dtype = np.uint8)

plt.close()
plt.close()

"""
Figure d'affichages par échelles de couleurs 
"""

fig = plt.figure("mes images")

plt.clf()  # Purge la figure

ax = fig.add_subplot(3,3,1)
ax.set_title("Image de base")
plt.imshow(im)
plt.colorbar()

ax = fig.add_subplot(3,3,2)
ax.set_title("Niveau de rouge")
plt.imshow(R, cmap=cm.Reds)
plt.colorbar()

ax = fig.add_subplot(3,3,3)
ax.set_title("Niveau de vert")
plt.imshow(G, cmap=cm.Greens)
plt.colorbar()

ax = fig.add_subplot(3,3,4)
ax.set_title("Niveau de bleu")
plt.imshow(B, cmap=cm.Blues)
plt.colorbar()

ax = fig.add_subplot(3,3,5)
ax.set_title("Bleu - Copper")
plt.imshow(B, cmap=cm.copper)
plt.colorbar()

ax = fig.add_subplot(3,3,6)
ax.set_title("Vert - Binary")
plt.imshow(G, cmap=cm.binary)
plt.colorbar()

ax = fig.add_subplot(3,3,7)
ax.set_title("Rouge - BuPu")
plt.imshow(R, cmap=cm.BuPu)
plt.colorbar()

ax = fig.add_subplot(3,3,8)
ax.set_title("Vert - OrRd")
plt.imshow(G, cmap=cm.OrRd)
plt.colorbar()

ax = fig.add_subplot(3,3,9)
ax.set_title("Rouge - YlOrBr")
plt.imshow(R, cmap=cm.YlOrBr)
plt.colorbar()

"""
Opérations de traitements d'images
"""

Z = R # On garde le canal Rouge
Zs = Z > 100

fig1 = plt.figure("operations")

plt.clf()  # Purge la figure

ax = fig1.add_subplot(2,2,1)
ax.set_title("Original")
plt.imshow(Z, cmap=cm.gray)
plt.colorbar()

ax = fig1.add_subplot(2,2,2)
ax.set_title("Seuil")
plt.imshow(Zs, cmap=cm.gray)
plt.colorbar()

ax = fig1.add_subplot(2,2,3)
ax.set_title("Histogramme")
plt.hist(Z.flatten(), bins=250)
plt.show()



