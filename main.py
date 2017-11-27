# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:06:13 2017

@author: hoferc
"""
import histogramme as histo
import telechargement as telg
import extract as ext
import bar

def main():
    # Telechargement
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2016/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2016.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2015/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2015.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2014/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2014.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2013.csv")
    donnees_2016 = ext.Extract('./2016.csv')
    dict_2016 = donnees_2016.build_dict()
    dict_2015 = ext.Extract('./2015.csv').build_dict()
    dict_2014 = ext.Extract('./2014.csv').build_dict()
    dict_2013 = ext.Extract('./2013.csv').build_dict()
    trafic_2016 = donnees_2016.get_trafic()
    
    stations_rer = ["GARE DU NORD-RER","GARE DE LYON-RER","LA DEFENSE-RER","CHATELET-LES HALLES-RER","NANTERRE-PREFECTURE"]
    stations_metro = ["GARE DU NORD","SAINT-LAZARE","GARE DE LYON","MONTPARNASSE-BIENVENUE","GARE DE L'EST"]
    stations_top5 = ["GARE DU NORD", "GARE DU NORD-RER", "SAINT-LAZARE", "GARE DE LYON-RER", "GARE DE LYON"]
    trafic_rer_2016 = []
    trafic_rer_2015 = []
    trafic_rer_2014 = []
    trafic_rer_2013 = []
    trafic_metro_2016 = []
    trafic_metro_2015 = []
    trafic_metro_2014 = []
    trafic_metro_2013 = []
    trafic_top5_2016 = []
    trafic_top5_2015 = []
    trafic_top5_2014 = []
    trafic_top5_2013 = []
    
    for rer in stations_rer:
        trafic_rer_2016.append((int)(dict_2016[rer].Trafic))
        trafic_rer_2015.append((int)(dict_2015[rer].Trafic))
        trafic_rer_2014.append((int)(dict_2014[rer].Trafic))
        trafic_rer_2013.append((int)(dict_2013[rer].Trafic))
        
    for metro in stations_metro:
        trafic_metro_2016.append((int)(dict_2016[metro].Trafic))
        trafic_metro_2015.append((int)(dict_2015[metro].Trafic))
        trafic_metro_2014.append((int)(dict_2014[metro].Trafic))
        trafic_metro_2013.append((int)(dict_2013[metro].Trafic))
        
    for station in stations_top5:
        trafic_top5_2016.append((int)(dict_2016[station].Trafic))
        trafic_top5_2015.append((int)(dict_2015[station].Trafic))
        trafic_top5_2014.append((int)(dict_2014[station].Trafic))
        trafic_top5_2013.append((int)(dict_2013[station].Trafic))
    
    b = list(range(0, 60000000, 5000000))

    ##On effectue le fiagramme uniquement pour l'année 2016 car les chiffres ne changent pas entre 2013 et 2016
    histo.Histogramme(trafic_2016, b, "Trafic", "Nb Stations", "Trafic gares RATP en 2016")
    bar.Bar(trafic_rer_2016, trafic_rer_2015, trafic_rer_2014, trafic_rer_2013, stations_rer, 'Stations', 'Trafic', 'Trafic Stations RER RATP')
    bar.Bar(trafic_metro_2016, trafic_metro_2015, trafic_metro_2014, trafic_metro_2013, stations_metro, 'Stations', 'Trafic', 'Trafic Stations Metro RATP')
    bar.Bar(trafic_top5_2016, trafic_top5_2015, trafic_top5_2014, trafic_top5_2013, stations_top5, 'Stations', 'Trafic', 'Trafic 5 Stations les plus fréquentées RATP')



if __name__ == "__main__":
    main()
