# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:11:15 2017

@author: Cassandra Hofer & Romain Lancia
"""

import folium

class Map_Idf:
    
    def __init__(self, liste_stations, dictio):
        self.dictio = dictio
        self.liste_stations = liste_stations
        self.genereMap()

    def genereMap(self):
        
        map_idf = folium.Map(location=[48.857426, 2.344295],
                           zoom_start=12)
        for station in self.liste_stations:
            if (int)(self.dictio[station].Accessibilite) >= 1:
                ic = 'ok'
                c = 'green'
            else:
                ic = 'remove'
                c = 'red'
            popup = folium.Popup(station, parse_html=True)
            
            folium.Marker([self.dictio[station].lat, self.dictio[station].long],
                          popup=popup,
                          icon=folium.Icon(color = c, icon = ic)).add_to(map_idf)
        print("Génération de la carte à l'adresse ./map.html")
        map_idf.save('./map.html')
        
