# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:19:12 2017

@author: Cassandra Hofer & Romain Lancia
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
        self.genereHistogramme()
        
    def genereHistogramme(self):
        
        n, bins, patches = plt.hist(self.trafic, bins=self.b,alpha = 0.9 ,color= ['crimson'], rwidth=0.9)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.text(25000000, 225, "Moyenne = {}\nMédiane = {}\nVariance = {}\nEcart type = {}".format(self.moyenne_histo(), self.mediane_histo(), self.variance_histo(), self.ecartType_histo()))
        print("Génération de l'histogramme à l'adresse ./charts/histo.png")
        plt.savefig("./charts/histo.png", dpi=150)
        
    def moyenne_histo(self):
        """
        Retourne la moyenne du trafic des gares de la RATP en 2016
    
        Returns:
            la moyenne en float
            
        >>> moyenne = moyenne_histo(trafic)
        >>> print(moyenne)
        4833226.92683
        """
        moyenne = np.mean(self.trafic)
        return moyenne
    
    def mediane_histo(self):
        """
        Retourne la mediane du trafic des gares de la RATP en 2016
    
        Returns:
            la mediane en float
            
        >>> mediane = mediane_histo(trafic)
        >>> print(mediane)
        3410557.0
        """
        mediane = np.median(self.trafic)
        return mediane
    
    def variance_histo(self):
        """
        Retourne la variance du trafic des gares de la RATP en 2016
    
        Returns:
            la variance en float
            
        >>> variance = variance_histo(trafic)
        >>> print(variance)
        3.5307850425e+13
        """
        variance = np.var(self.trafic)
        return variance
        
    def ecartType_histo(self):
        """
        Retourne l'ecart type du trafic des gares de la RATP en 2016
    
        Returns:
            l'ecart type en float
            
        >>> ecartType = ecartType_histo(trafic)
        >>> print(ecartType)
        5942040.93094
        """
        ecartType = np.std(self.trafic)
        return ecartType
