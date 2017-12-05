"""
Created on Wed Nov  8 10:45:30 2017

@author: Cassandra Hofer & Romain Lancia
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
        self.genereBar()
        
    def genereBar(self):
        """
        Génere un bar graphe à l'aide des paramétres de l'objet courant puis
        le sauvegarde au nom de son titre au format png dans le dossier ./charts
        """
        nb_stations = len(self.labels)
        # create plot
        fig, ax = plt.subplots()
        index = np.arange(nb_stations)
        bar_width = 0.15
        opacity = 0.8

        # bars pour les valeurs de 2016
        rects1 = plt.bar(index, self.w, bar_width,
                         alpha=opacity,
                         color='darkorange',
                         label='2016')
         
       # bars pour les valeurs de 2015
        rects2 = plt.bar(index + bar_width, self.x, bar_width,
                         alpha=opacity,
                         color='crimson',
                         label='2015')

        # bars pour les valeurs de 2014
        rects3 = plt.bar(index + bar_width *2 , self.y, bar_width,
                         alpha=opacity,
                         color='sandybrown',
                         label='2014')
         
        # bars pour les valeurs de 2013
        rects4 = plt.bar(index + bar_width *3, self.z, bar_width,
                         alpha=opacity,
                         color='darkred',
                         label='2013')
         
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        # Les noms des stations étant pour certains très longs pour éviter un chevochement
        #on effectue une rotation sur les valeurs de x et on réduit egalement la taille de la police
        plt.xticks(index + 3*bar_width/2 , self.labels,fontsize = 8, rotation=12)
        #affichage de la légende
        plt.legend()
         
        plt.tight_layout()
        print("Génération du bar chart {} à l'adresse ./charts/{}.png".format(self.title, self.title))
        fig.savefig("./charts/"+self.title+'.png', dpi = 150)
        
        
