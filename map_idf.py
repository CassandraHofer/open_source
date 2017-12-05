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
        """
        Génere la map enregistrée dans le fichier ./map_idf.html
        """
        #Choix des coordonnées servant à centrer la carte sur Paris ainsi que du zoom de la carte
        map_idf = folium.Map(location=[48.857426, 2.344295],
                           zoom_start=12)
        # Ajout d'un point sur la map pour chaque station de la liste du fichier courant
        for station in self.liste_stations:
            if (int)(self.dictio[station].Accessibilite) >= 1:
                # Marqueur vert si la station est accessible
                ic = 'ok'
                c = 'green'
            else:
                #Marqueur rouge sinon
                ic = 'remove'
                c = 'red'
            popup = folium.Popup(station, parse_html=True)
            
            folium.Marker([self.dictio[station].lat, self.dictio[station].long],
                          popup=popup,
                          icon=folium.Icon(color = c, icon = ic)).add_to(map_idf)
        print("Génération de la carte à l'adresse ./map.html")
        map_idf.save('./map.html')
        
