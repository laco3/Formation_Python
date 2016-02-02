# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 10:37:54 2016

@author: laco3
"""

def fonction(x, y, z, *args, **kwargs): #permet de créer des fct fourre tout qui accepte tout type d'arguments sans spec
  print x, y, z
  print args, kwargs
  
fonction(1,2,3, 5, truck = 36)
fonction(1,2, z=5, truc = 36, machin = 12)

def somme(*args, **kwargs):
  return sum(args) + sum(kwargs.values())
  
print somme(3, 5, 12, x = 36, y = 32)

def fonc(lapin, pomme):
  print lapin, pomme

fonc(4,5)

def print_keyword_args(**dic):
  # dic is a dict of the keyword args passed to the function
  for key, value in dic.iteritems():
    print "%s = %s" % (key, value)
         
dic = {"pomme" : "pourrie", "lapin" : "oreilles"}

fonc(**dic) # Affiche les mots de dic associés à ceux de fonc 

print_keyword_args(**dic) # Affiche la correspondance entre les mots de dic

