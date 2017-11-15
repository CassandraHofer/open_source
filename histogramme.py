"""
Created on Wed Nov  8 10:45:30 2017

@author: hoferc
"""

import numpy as np # import package
import matplotlib.pyplot as plt

class Histogramme:
    def __init__(self, w, x, y, z, b, xlabel, ylabel, tittle):
        #Faire de x, y, etc des dico contenant label et la liste de valeurs
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.b = b
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.tittle = tittle
        
    def afficherHistogramme(self):
        data = np.vstack([self.w, self.x, self.y, self.z]).T
                        
        #b = ["Gare de Lyon", "Montparnasse", "La Rochelle"];
        n, bins, patches = plt.hist(data, bins=self.b, label= ['2013','2014','2015','2016'], color= ['crimson', 'burlywood', 'darkmagenta', 'olive'])
        
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend(loc='upper right')
        plt.title(self.tittle)
        plt.show()