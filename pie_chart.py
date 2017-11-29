# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:53:36 2017

@author: hoferc
"""
import matplotlib.pyplot as plt

class Pie_Chart:
    def __init__(self, title, labels, lst):
        self.title = title
        self.labels = labels
        self.lst = lst
        self.afficherPieChart()


    def afficherPieChart(self):
        labels = 'Python', 'C++', 'Ruby', 'Java'
        sizes = [215, 130, 245, 210]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        explode = (0.1, 0, 0, 0)  # explode 1st slice
         
        # Plot
        plt.figure()
        plt.title(self.title)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)
         
        plt.axis('equal')
        plt.tight_layout()
        #plt.show()
        plt.savefig(self.title + ".png")