# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:53:36 2017

@author: Cassandra Hofer & Romain Lancia
"""
import matplotlib.pyplot as plt

class Pie_Chart:
    def __init__(self, title, labels, lst):
        self.title = title
        self.labels = labels
        self.lst = lst
        self.generePieChart()


    def generePieChart(self):
        """
        Génere un pie chart en fonction des valeur de lst en paramétre de l'objet
        courant puis le sauvegarde sous format png à l'adresse ./charts/pie.png
        """
        count_access = 0;
        count_non_access = 0;
        for e in self.lst:
            if e>=1 :
                count_access += 1
            else :
                count_non_access += 1
        sizes = [count_access, count_non_access]
        colors = ['lightcoral', 'lightskyblue']
        explode = (0.1, 0)  # explode 1st slice
         
        # Creation d'une nouvelle figure
        plt.figure()
        plt.title(self.title)
        plt.pie(sizes, explode=explode, labels=self.labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)
         
        plt.axis('equal')
        plt.tight_layout()
        print("Génération du pie chart à l'adresse ./charts/pie.png")
        plt.savefig("./charts/pie.png", dpi = 150)
