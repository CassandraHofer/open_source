# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:06:13 2017

@author: hoferc
"""
import numpy as np

import histogramme_bar as histo
import telechargement as telg
import extract as ext

def main():
    # Telechargement
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2016/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2016.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2015/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2015.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2014/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2014.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2013.csv")
    trafic_2016 = ext.Extract('./2016.csv').get_trafic()
    
    
#    donnees_2015 = ext('./2015.csv').build_dict()
#    donnees_2014 = ext('./2014.csv').build_dict()
#    donnees_2013 = ext('./2013.csv').build_dict()
    
#    stations_diag_metro = ("GARE DU NORD","SAINT-LAZARE","GARE DE LYON","MONTPARNASSE-BIENVENUE","GARE DE L'EST")
#    stations_diag_rer = ("GARE DU NORD-RER","GARE DE LYON-RER","LA DEFENSE-RER","CHATELET-LES-HALLES-RER","NANTERRE-PREFECTURE")
    
#    print(donnees_2016['GARE DE LYON'])
#    print(donnees_2016['NOISY-CHAMPS'])
#    print(donnees_2016['GARE DE LYON'].Trafic)
#    print(donnees_2016['NOISY-CHAMPS'].Rang)
#    print(donnees_2016['NOISY-CHAMPS'].Ville)
#    print('Done')
    for e in trafic_2016:
        print(e)
        
    count0_10 = 0
    count10_20 = 0
    count20_30 = 0
    count30_40 = 0
    count40_50 = 0
    count50_60 = 0
    for trafic in trafic_2016:
        if trafic < 10000000:
            count0_10 += 1
        elif trafic < 20000000:
            count10_20 += 1
        elif trafic < 30000000:
            count20_30 += 1
        elif trafic < 40000000:
            count30_40 += 1
        elif trafic < 50000000:
            count40_50 += 1
        elif trafic < 60000000:
            count50_60 += 1
    print("\n")        
    print(count0_10)
    print(count10_20)
    print(count20_30)
    print(count30_40)
    print(count40_50)
    print(count50_60)
        
        
    
    w = np.random.randn(10000)
    x = np.random.randn(10000)
    y = np.random.randn(10000)
    z = np.random.randn(10000)
    
    b = list(range(-4,5,1))

    histogramme = histo.Histogramme_Bar(w, x, y, z, b, "bins", "count", "10.000 random numbers")
    histogramme.afficherHistogramme()
    

if __name__ == "__main__":
    main()
