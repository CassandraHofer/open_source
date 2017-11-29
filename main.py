# encoding: utf8
"""
Created on Wed Nov 15 09:06:13 2017

@author: hoferc
"""
import histogramme as histo
import telechargement as telg
import extract as ext
import bar
import pie_chart as pc
import pip
import map_idf
import webbrowser
import os

def main():
    # Telechargement
    pip.main(['install', 'folium'])
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2016/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2016.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2015/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2015.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2014/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2014.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./2013.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/accessibilite-des-gares-et-stations-metro-et-rer-ratp/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "./access.csv")
    donnees_2016 = ext.Extract('./2016.csv')
    dict_2016 = donnees_2016.build_dict_trafic()
    dict_2015 = ext.Extract('./2015.csv').build_dict_trafic()
    dict_2014 = ext.Extract('./2014.csv').build_dict_trafic()
    dict_2013 = ext.Extract('./2013.csv').build_dict_trafic()
    trafic_2016 = donnees_2016.get_trafic()
    donnees_accessibilite = ext.Extract('./access.csv')
    dict_accessibilite = donnees_accessibilite.build_dict_accessibilite()
    lst_accessibilite = donnees_accessibilite.get_accessibilite()
    
    
    stations_rer = ["GARE DU NORD-RER","GARE DE LYON-RER","LA DEFENSE-RER","CHATELET-LES HALLES-RER","NANTERRE-PREFECTURE"]
    stations_metro = ["GARE DU NORD","SAINT-LAZARE","GARE DE LYON","MONTPARNASSE-BIENVENUE","GARE DE L'EST"]
    stations_top5 = ["GARE DU NORD", "GARE DU NORD-RER", "SAINT-LAZARE", "GARE DE LYON-RER", "GARE DE LYON"]
    stations_map = ['Porte de Vincennes', 'Gare de Lyon', 'Tuileries', 'Grands Boulevards', 'Billancourt', 'Aubervilliers Pantin (4 Chemins)', 'Porte d\'Italie', 'Pont Neuf', 'Montparnasse-Bienvenue', 'Les Halles', 'Bercy']
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
    pc.Pie_Chart("Accessibilite des Gare RATP", ["Accessible", "Non Accessible"], lst_accessibilite)
    map_idf.Map_Idf(stations_map, dict_accessibilite)
    webbrowser.open(os.getcwd()+"/map.html")


if __name__ == "__main__":
    main()
