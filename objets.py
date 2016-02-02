# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 09:06:23 2016

@author: laco3
"""

import numpy as np

"""
v = np.array([0.,1.,0.])
u = np.array([1.,0.,0.])
"""

"""
print u.cross(v)
print v.cross(u)
"""


class Vector(object): #Création d'une classe
  
  def __init__(self, x=0, y=0, z=0): # Définition des arguments et de leur initialisation
    self.coords = np.array([x, y, z])
  
  def __repr__(self): # Definition de ce qui s'affiche quand on appelle la représentation de la classe
    c = self.coords
    return "<Vecteur : ({0}, {1}, {2})>".format(c[0], c[1], c[2])
  
  def norme(self):
    return (self.coords**2).sum()**.5
    
  def normaliser(self):
    n = self.norme()
    self.coords /= n

  def __mul__(self, other): # On définit ce qui se passe quand on multiplie le vecteur
    out = Vector()
    if isinstance(other, Vector): # Définition de ce qu'il se passe si on multiplie 2 vecteurs
      out.coords = np.cross(self.coords, other.coords)
    else:
      out.coords = self.coords * other
    return out
    
  __rmul__ = __mul__ #Commutativité de la multiplication

u = Vector(1., 0., 0.)
v = Vector(5., 4., 2.)

"""
Main
"""

print "\n"
print "Multiplication de v par 2 :"
print v * 2

print "\n"
print "Multiplication de 2 par v (commutativité):"
print 2 * v

print "\n"
print "Multiplication de v par u :"
print v * u

print "\n"
print "v est-il un vecteur ?"
print isinstance (v, Vector)
print "\n"
print "2 est-il un vecteur ?"
print isinstance (2, Vector)