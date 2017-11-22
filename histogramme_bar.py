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
        data = np.vstack([self.w, self.x, self.y, self.z]).T
                        
        n, bins, patches = plt.hist(data, bins=self.b, label= ['2013','2014','2015','2016'], color= ['crimson', 'burlywood', 'darkmagenta', 'olive'])
        
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend(loc='upper right')
        plt.title(self.tittle)
        plt.show()
        
        
    def afficherBar(self):
        
        self.x = (20, 35, 30, 35)

        self.y = (25, 32, 34, 20)

        self.z = (25, 32, 34, 20)

        fig, ax = plt.subplots()

        index = np.arange(4)
        bar_width = 0.25

        opacity = 0.4

        rects1 = plt.bar(index, self.x, bar_width,
                         alpha=opacity,
                         color='b',
                         label='Men')

        rects2 = plt.bar(index + bar_width, self.y, bar_width,
                         alpha=opacity,
                         color='r',
                         label='Women')

        rects2 = plt.bar(index + bar_width*2, self.z, bar_width,
                         alpha=opacity,
                         color='y',
                         label='Women')
        
        plt.xlabel('Group')
        plt.ylabel('Scores')
        plt.title('Scores by group and gender')
        plt.xticks(index + bar_width / 2, ('A', 'B', 'C', 'D'))
        plt.legend()

        plt.tight_layout()
        plt.show()