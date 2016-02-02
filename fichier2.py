# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 15:25:44 2016

@author: laco3
"""

import numpy as np
import pickle

"""
pickle permet d'enregistrer des données pour les recharger plus tard
"""

data = ["truck", "machin", [1,2,3]]

f = open("data.pckl", "w")
pickle.dump(data, f, 2)
f.close

del data #On efface fonc

f = open("data.pckl")
data2=pickle.load(f)
f.close