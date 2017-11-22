# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:06:13 2017

@author: hoferc
"""
import numpy as np

import histogramme as histo
import telechargement as telg
import extract as ext

def main():
    
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2016/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2016.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2015/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2015.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2014/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2014.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2013.csv")
    donnees_2016 = ext.build_dict('./2016.csv')
    donnees_2015 = ext.build_dict('./2015.csv')
    donnees_2014 = ext.build_dict('./2014.csv')
    donnees_2013 = ext.build_dict('./2013.csv')
    
    stations_diag_metro = ("GARE DU NORD","SAINT-LAZARE","GARE DE LYON","MONTPARNASSE-BIENVENUE","GARE DE L'EST")
    stations_diag_rer = ("GARE DU NORD-RER","GARE DE LYON-RER","LA DEFENSE-RER","CHATELET-LES-HALLES-RER","NANTERRE-PREFECTURE")
    
    w = np.random.randn(10000)
    x = np.random.randn(10000)
    y = np.random.randn(10000)
    z = np.random.randn(10000)
    
    b = list(range(-4,5,1))

    histogramme = histo.Histogramme_Bar(w, x, y, z, b, "bins", "count", "10.000 random numbers")
    histogramme.afficherHistogramme()

if __name__ == "__main__":
    main()
