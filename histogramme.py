# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:19:12 2017

@author: hoferc
"""

import numpy as np # import package
import matplotlib.pyplot as plt

class Histogramme:
    def __init__(self, trafic, b, xlabel, ylabel, title):
        self.trafic = trafic
        self.b = b
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
        self.afficherHistogramme()
        
    def afficherHistogramme(self):
        n, bins, patches = plt.hist(self.trafic, bins=self.b,alpha = 0.9 ,color= ['crimson'] , rwidth=0.9)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        #plt.show()
        plt.savefig(self.title + ".png")
