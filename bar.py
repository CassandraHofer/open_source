"""
Created on Wed Nov  8 10:45:30 2017

@author: hoferc
"""

import numpy as np # import package
import matplotlib.pyplot as plt

class Bar:
    def __init__(self, w, x, y, z, labels, xlabel, ylabel, tittle):
        self.w = w
        self.x = x  
        self.y = y
        self.z = z
        self.labels = labels
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.tittle = tittle    
        self.afficherBar()
        
    def afficherBar(self):

        n_groups = 5
        means_frank = self.w
        means_guido = self.x
        frank = self.y
        guido = self.z
         
        # create plot
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.10
        opacity = 0.8
         
        rects1 = plt.bar(index, means_frank, bar_width,
                         alpha=opacity,
                         color='b',
                         label='Frank')
         
        rects2 = plt.bar(index + bar_width, means_guido, bar_width,
                         alpha=opacity,
                         color='g',
                         label='Guido')
        
        rects3 = plt.bar(index + bar_width *2 , frank, bar_width,
                         alpha=opacity,
                         color='y',
                         label='Robert')
         
        rects4 = plt.bar(index + bar_width *3, guido, bar_width,
                         alpha=opacity,
                         color='r',
                         label='George')
         
        plt.xlabel('Person')
        plt.ylabel('Scores')
        plt.title('Scores by person')
        plt.xticks(index + bar_width*2, ('A', 'B', 'C', 'D'))
        plt.legend()
         
        plt.tight_layout()
        plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
#        fig, ax = plt.subplots()
#
#        index = np.arange(4)
#        
#        bar_width = 0.20
#
#        opacity = 0.4
#
#        trafic2016 = plt.bar(range(len(self.x)), self.x, bar_width,
#                         alpha=opacity,
#                         color='b',
#                         label='2016')
#
#        trafic2015 = plt.bar(range(len(self.y)) + bar_width, self.y, bar_width,
#                         alpha=opacity,
#                         color='r',
#                         label='2015')
#
#        trafic2014 = plt.bar(range(len(self.z)) + bar_width*2, self.z, bar_width,
#                         alpha=opacity,
#                         color='y',
#                         label='2014')
#        
#        trafic2013 = plt.bar(range(len(self.z)) + bar_width*3, self.z, bar_width,
#                         alpha=opacity,
#                         color='y',
#                         label='2013')
#        
#        
#        
#        plt.xlabel('Group')
#        plt.ylabel('Scores')
#        plt.title('Scores by group and gender')
#        plt.xticks(index + bar_width / 4, ('A', 'B', 'C', 'D'))
#        plt.legend()
#
#        plt.tight_layout()
#        plt.show()
