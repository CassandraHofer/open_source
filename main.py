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
    trafic_2015 = ext.Extract('./2015.csv').get_trafic()
    trafic_2014 = ext.Extract('./2014.csv').get_trafic()
    trafic_2013 = ext.Extract('./2013.csv').get_trafic()
    
    
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

    b = list(range(0, 60000000, 5000000))

    histo_bar = histo.Histogramme_Bar(trafic_2016, trafic_2015, trafic_2014, trafic_2013, b, "Trafic", "Nb Stations", "Trafic gares RATP")
    histo_bar.afficherHistogramme()
    histo_bar.afficherBar()

if __name__ == "__main__":
    main()
