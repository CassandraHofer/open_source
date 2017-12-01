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
        self.afficherHistogramme()
        self.moyenne_histo(trafic)
        self.mediane_histo(trafic)
        self.variance_histo(trafic)
        self.ecartType_histo(trafic)
        
        
    def afficherHistogramme(self):
        
        n, bins, patches = plt.hist(self.trafic, bins=self.b,alpha = 0.9 ,color= ['crimson'] , rwidth=0.9)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.savefig("./charts/histo.png", dpi=150)
        
    def moyenne_histo(self, liste):
        """
        Retourne la moyenne du trafic des gares de la RATP en 2016
    
        Args:
            liste: liste du trafic de chaque station de la RATP en 216
    
        Returns:
            la moyenne en float
            
        >>> moyenne = moyenne_histo(trafic)
        >>> print(moyenne)
        4833226.92683
        """
        moyenne = np.mean(liste)
        return moyenne
    
    def mediane_histo(self, liste):
        """
        Retourne la mediane du trafic des gares de la RATP en 2016
    
        Args:
            liste: liste du trafic de chaque station de la RATP en 216
    
        Returns:
            la mediane en float
            
        >>> mediane = mediane_histo(trafic)
        >>> print(mediane)
        3410557.0
        """
        mediane = np.median(liste)
        return mediane
    
    def variance_histo(self, liste):
        """
        Retourne la variance du trafic des gares de la RATP en 2016
    
        Args:
            liste: liste du trafic de chaque station de la RATP en 216
    
        Returns:
            la variance en float
            
        >>> variance = variance_histo(trafic)
        >>> print(variance)
        3.5307850425e+13
        """
        variance = np.var(liste)
        return variance
        
    def ecartType_histo(self, liste):
        """
        Retourne l'ecart type du trafic des gares de la RATP en 2016
    
        Args:
            liste: liste du trafic de chaque station de la RATP en 216
    
        Returns:
            l'ecart type en float
            
        >>> ecartType = ecartType_histo(trafic)
        >>> print(ecartType)
        5942040.93094
        """
        ecartType = np.std(liste)
        return ecartType