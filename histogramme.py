"""
Created on Wed Nov  8 10:45:30 2017

@author: hoferc
"""

import numpy as np # import package
import matplotlib.pyplot as plt # import module

x = np.random.randn(10000)
y = np.random.randn(10000)
a = np.random.randn(10000)
b = np.random.randn(10000)
data = np.vstack([x, y, a, b]).T

b = list(range(-4,5,1))

n, bins, patches = plt.hist(data, bins=b,label=['x','y','a','b'], color=['crimson', 'burlywood', 'darkmagenta', 'olive'])

plt.xlabel('bins')
plt.ylabel('count')
plt.legend(loc='upper right')
plt.title('10.000 random numbers')

plt.show()

class Histogramme:
    def __init__(self, x, y= null, a= null, b= null, xlabel, ylabel, tittle):
        #Faire de x, y, etc des dico contenant label et la liste de valeurs
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.tittle = tittle
    def creerHisto(self):
        if b != null :
            data = np.vstack([x, y, a, b]).T
            label = ['x','y','a','b']                
        elif a != null:
            data = np.vstack([x, y, a]).T
            label = ['x','y','a','b']  
        elif y != null:
            data = np.vstack([x, y]).T
        
        