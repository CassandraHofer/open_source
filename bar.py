"""
Created on Wed Nov  8 10:45:30 2017

@author: hoferc
"""

import numpy as np # import package
import matplotlib.pyplot as plt

class Bar:
    def __init__(self, w, x, y, z, labels, xlabel, ylabel, title):
        self.w = w
        self.x = x  
        self.y = y
        self.z = z
        self.labels = labels
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title    
        self.afficherBar()
        
    def afficherBar(self):
        
        nb_stations = len(self.labels)
        # create plot
        fig, ax = plt.subplots()
        index = np.arange(nb_stations)
        bar_width = 0.15
        opacity = 0.8
        
        rects1 = plt.bar(index, self.w, bar_width,
                         alpha=opacity,
                         color='b',
                         label='2016')
         
        rects2 = plt.bar(index + bar_width, self.x, bar_width,
                         alpha=opacity,
                         color='g',
                         label='2015')
        
        rects3 = plt.bar(index + bar_width *2 , self.y, bar_width,
                         alpha=opacity,
                         color='y',
                         label='2014')
         
        rects4 = plt.bar(index + bar_width *3, self.z, bar_width,
                         alpha=opacity,
                         color='r',
                         label='2013')
         
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.xticks(index + 3*bar_width/2 , self.labels,fontsize = 8)
        plt.legend()
         
        plt.tight_layout()
        #plt.show()
        fig.savefig(self.title+'.png', dpi = 150)
        
        
