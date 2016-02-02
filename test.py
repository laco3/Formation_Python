# -*- coding: utf-8 -*-
"""
@title : Formation Python SISEO - 01/02/2016

@author :  Thomas Lacombe
"""

import numpy as np
import matplotlib.pyplot as plt

def mafonction(x):
    
  """
  
  Une fonction mathématique 
  
  Entrées :
  * x: une variable
  
  Renvoie : le carré de x
  
  """
  
  """
  ATTENTION : la position du premier caractère est importante (indentation)
  
  """
  
  return x**2 # le carré de x
  
print "Calcul de la focntion avec x = 6 :"
print mafonction(6) # execute la fonction

print "Help de la fonction :"
print help(mafonction) # affiche l'aide de la fonction (commentaire au début de la fonction)

print "Méthodes internes utilisées :"
print dir(mafonction) # méthodes internes à python

"""
Création d'une liste
"""
x = [1,2,3]

print "Type de la liste x :"
print type(x)

print"Affiche les valeurs des indices 0, 1 et 2 de la liste x :"
print x[0] # Commence à indice 0
print x[1]
print x[2]

print"Affiche les valeurs des indices -1 et -2 de la liste x :"
print x[-1]
print x[-2]

print "Coupe la liste après la 2ème valeur :"
print x[:2]

print "Concatène la liste avec elle-même :"
print x*2  # Concaténation de la même liste à la suite

x.append("tutu") #ajout d'une chaine de caratcère à la liste
x.append(mafonction) #ajout d'une fonction à la liste 

print x


"""
Création d'un array de liste avec numpy (bilio orientée calcul scientifique)
"""
y = np.array([1,2,3])

print type(y)

print y[1]
print y*2  # Multiplication terme à terme


"""
Figure
"""

x = np.linspace(0., 10., 11)
y = mafonction(x)

#Tracé de la figure (ouvre directement une autre fenêtre à l'exécution)
plt.figure("Une figure")
plt.clf()  # Purge la figure
plt.plot(x, y)
plt.grid()
plt.xlabel("Temps, $t$ [s]")
plt.ylabel("Amplitudes, $a$ [N]")
plt.show()
