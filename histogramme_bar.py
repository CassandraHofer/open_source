"""
Created on Wed Nov  8 10:45:30 2017

@author: hoferc
"""

import numpy as np # import package
import matplotlib.pyplot as plt

class Histogramme_Bar:
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
                        
        n, bins, patches = plt.hist(self.w, bins=self.b,alpha = 0.9 ,color= ['crimson'] , rwidth=0.9)

        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend(loc='upper right')
        plt.title(self.tittle + " en 2016" )
        plt.show()
        
        
    def afficherBar(self):

        fig, ax = plt.subplots()

        index = np.arange(4)
        
        bar_width = 0.20

        opacity = 0.4

        trafic2016 = plt.bar(index, self.x, bar_width,
                         alpha=opacity,
                         color='b',
                         label='2016')

        trafic2015 = plt.bar(index + bar_width, self.y, bar_width,
                         alpha=opacity,
                         color='r',
                         label='2015')

        trafic2014 = plt.bar(index + bar_width*2, self.z, bar_width,
                         alpha=opacity,
                         color='y',
                         label='2014')
        
        trafic2013 = plt.bar(index + bar_width*3, self.z, bar_width,
                         alpha=opacity,
                         color='y',
                         label='2013')
        
        
        
        plt.xlabel('Group')
        plt.ylabel('Scores')
        plt.title('Scores by group and gender')
        plt.xticks(index + bar_width / 4, ('A', 'B', 'C', 'D'))
        plt.legend()

        plt.tight_layout()
        plt.show()