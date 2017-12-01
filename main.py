# encoding: utf8
"""
Created on Wed Nov 15 09:06:13 2017

@author: hoferc
"""

import pip
pip.main(['install', 'folium'])
import histogramme as histo
import telechargement as telg
import extract as ext
import bar
import pie_chart as pc

import map_idf
import webbrowser
import os

def main():
    # Telechargement
    
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2016/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "csv/2016.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2015/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "csv/2015.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2014/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "csv/2014.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "csv/2013.csv")
    telg.Telechargement("https://data.ratp.fr/explore/dataset/accessibilite-des-gares-et-stations-metro-et-rer-ratp/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", "csv/access.csv")
    donnees_2016 = ext.Extract('csv/2016.csv')
    dict_2016 = donnees_2016.build_dict_trafic()
    dict_2015 = ext.Extract('csv/2015.csv').build_dict_trafic()
    dict_2014 = ext.Extract('csv/2014.csv').build_dict_trafic()
    dict_2013 = ext.Extract('csv/2013.csv').build_dict_trafic()
    trafic_2016 = donnees_2016.get_trafic()
    donnees_accessibilite = ext.Extract('csv/access.csv')
    dict_accessibilite = donnees_accessibilite.build_dict_accessibilite()
    lst_accessibilite = donnees_accessibilite.get_accessibilite()
    
    
    stations_rer = ["GARE DU NORD-RER","GARE DE LYON-RER","LA DEFENSE-RER","CHATELET-LES HALLES-RER","NANTERRE-PREFECTURE"]
    stations_metro = ["GARE DU NORD","SAINT-LAZARE","GARE DE LYON","MONTPARNASSE-BIENVENUE","GARE DE L'EST"]
    stations_top5 = ["GARE DU NORD", "GARE DU NORD-RER", "SAINT-LAZARE", "GARE DE LYON-RER", "GARE DE LYON"]
    stations_map = ['Porte de Vincennes', 'Gare de Lyon', 'Tuileries', 'Grands Boulevards', 'Billancourt', 'Aubervilliers Pantin (4 Chemins)', 'Porte d\'Italie', 'Pont Neuf', 'Montparnasse-Bienvenue', 'Les Halles', 'Bercy', 'Porte de Clignancourt', 'Riquet', 'Nogent-sur-Marne', 'Gare du Nord', 'Passy', 'Drancy', 'Saint-Lazare', 'Val de Fontenay', 'Place de Clichy', 'Rueil-Malmaison', 'Boulogne Pont de Saint-Cloud', 'Chatou-Croissy', 'Porte des Lilas', 'Denfert-Rochereau', 'Oberkampf', 'Porte de Saint-Ouen', 'Arcueil-Cachan', 'Joinville-le-Pont', 'Charenton-Ecoles', 'Porte de Versailles', 'Bagneux', 'Mairie de Clichy', 'Mairie de Montreuil', 'Rue des Boulets', 'Pont de Neuilly', 'Nanterre-Préfecture']
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

    
    ##On effectue le diagramme uniquement pour l'année 2016 car les chiffres ne changent pas entre 2013 et 2016
    histo.Histogramme(trafic_2016, b, "Trafic (par pas de 5 millions)", "Nombre de stations", "Trafic de l'ensemble des gares RATP en 2016")
    bar.Bar(trafic_rer_2016, trafic_rer_2015, trafic_rer_2014, trafic_rer_2013, stations_rer, 'Stations', 'Trafic (en millions)', 'Trafic des 5 stations RER les plus fréquentées de la RATP')
    bar.Bar(trafic_metro_2016, trafic_metro_2015, trafic_metro_2014, trafic_metro_2013, stations_metro, 'Stations', 'Trafic (en millions)', 'Trafic des 5 stations Métro les plus fréquentées de la RATP')
    bar.Bar(trafic_top5_2016, trafic_top5_2015, trafic_top5_2014, trafic_top5_2013, stations_top5, 'Stations', 'Trafic (en millions)', 'Trafic des 5 stations les plus fréquentées de la RATP')
    pc.Pie_Chart("Accessibilité pour les personnes à mobilité réduite des gares RATP", ["Accessibles", "      Non\nAccessibles"], lst_accessibilite)
    map_idf.Map_Idf(stations_map, dict_accessibilite)
    webbrowser.open(os.getcwd()+"./index.html") 


if __name__ == "__main__":
    main()
