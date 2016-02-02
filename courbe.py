# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 11:24:19 2016

@author: laco3
"""

import numpy as np
import matplotlib.pyplot as plt

def mafonction2(t, omega=1., tau=10.):
    
  """
  
  Une fonction mathématique 
  
  Entrées :
  * t: une variable
  * omega : pulsation
  * tau : temps caractéristique
  
  Renvoie : 
  Une sinusoïdale amortie. 
  
  """
  
  return np.exp(-t / tau) * np.sin(omega * t)
  
t = np.linspace(0., 20., 1000)
#a = mafonction2(t)
omega = range(10) # valeurs de omega
  
 # Tracé de la figure
colors = "ygcmkrbg"
plt.figure("Une figure")
plt.clf()  # Purge la figure
for i in xrange(len(omega)): # xrange = range mais en prenant moins de mémoire
  o = omega[i]
  c = colors[i%len(colors)]
  a = mafonction2(t, omega = o)
  plt.plot(t, a, color = c, label = "$\omega = {0:.0f}$".format(o))
plt.legend()
plt.grid()
plt.xlabel("Temps, $t$ [s]")
plt.ylabel("Amplitudes, $a$ [N]")
plt.show()
