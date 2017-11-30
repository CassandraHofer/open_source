# encoding: utf8
"""
Created on Tue Nov 21 21:58:03 2017

@author: romain
"""

import csv
from collections import namedtuple
from unidecode import unidecode


class Extract:
    
    def __init__(self, csvfile):
        self.csvfile = csvfile
        
        
    def build_dict_trafic(self):
        """
        retourne un dictionnaire des stations de transports en commun du fichier passé en argument
    
        Args:
            csvfile: un fichier au format csv contenant une liste de stations de transports en commun
    
        Returns:
            dictionnaire de namedtuple des informations relatives aux stations de transports en commun
            
        >>> d = build_hist_dict('trafic-annuel-entrant-par-station-du-reseau-ferre-2016.csv')
        >>> print(d['GARE DE LYON'])
        Station(Trafic='36352115', Rang='3', Ville='Paris')
        >>> print(d['NOISY-CHAMPS'])
        Station(Trafic='4868790', Rang='20', Ville='Champs-sur-Marne')
        >>> print(d['GARE DE LYON'].Trafic)
        36352115
        >>> print(d['NOISY-CHAMPS'].Ville)
        Champs-sur-Marne
        """
        
        # Construire le namedtuple
        Station = namedtuple('Station', ['Trafic', 'Rang', 'Ville'])
        # Crée un dictionnaire vide pour stocker les données
        d = dict()
        # pour chaque ligne on ajoute au dictionnaire une paire clé-valeur
        # la clé est construite avec une information contenue dans la ligne
        # la valeur est le namedtuple Station dont les champs sont contenus dans la ligne
        with open(self.csvfile) as f:
            reader = csv.DictReader(f, delimiter=';')
            for ligne in reader:
                d[ligne['Station']] = Station(ligne['Trafic'], ligne['Rang'], ligne['Ville'])       
        return d
    
    
    def get_trafic(self):
        
        lst_trafic = []
        stations = self.build_dict_trafic()
        for station in stations.keys():
            lst_trafic.append((int)(stations[station].Trafic))
                
        return lst_trafic

    def build_dict_accessibilite(self):
        Station = namedtuple('nomptar', ['Accessibilite', 'lat', 'long'])
        # Crée un dictionnaire vide pour stocker les données
        d = dict()
        # pour chaque ligne on ajoute au dictionnaire une paire clé-valeur
        # la clé est construite avec une information contenue dans la ligne
        # la valeur est le namedtuple Station dont les champs sont contenus dans la ligne
        with open(self.csvfile) as f:
            reader = csv.DictReader(f, delimiter=';')
            for ligne in reader:
                ligne['nomptar'] = unidecode(ligne['nomptar'])
                lat, long = ligne['coord'].split(', ')
                d[ligne['nomptar']] = Station(ligne['Accessibilite Quai Train'], (float)(lat), (float)(long))                
        return d
    
    def get_accessibilite(self):
        lst_accessibilite = []
        stations = self.build_dict_accessibilite()
        for station in stations.keys():
            lst_accessibilite.append((int)(stations[station].Accessibilite))
                
        return lst_accessibilite
