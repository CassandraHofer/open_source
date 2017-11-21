# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:58:03 2017

@author: romain
"""

import csv, json
from collections import namedtuple

def build_hist_dict(csvfile):
    """
    retourne un dictionnaire des stations de transports en commun du fichier passé en argument

    Args:
        csvfile: un fichier au format csv contenant une liste de stations de transports en commun

    Returns:
        dictionnaire de namedtuple des informations relatives aux stations de transports en commun
        
    >>> d = build_stations_dict('stations-meteo.csv')
    >>> print(d['NICE'])
    Station(ID='07690', Latitude=43.648833, Longitude=7.209, Altitude=2)
    >>> print(d['BELLE ILE-LE TALUT'])
    Station(ID='07207', Latitude=47.294333, Longitude=-3.218333, Altitude=34)
    >>> print(d['CAYENNE-MATOURY'])
    Station(ID='81405', Latitude=4.822333, Longitude=-52.365333, Altitude=4)
    >>> print(d['NICE'].Latitude)
    43.648833
    """
    
    # Construire le namedtuple
    Station = namedtuple('Station', ['Trafic', 'Rang', 'Ville'])
    # CrÃ©er un dictionnaire vide pour stocker les donnÃ©es
    d = dict()
    # ouvrir le fichier csv
    # utiliser un objet DictReader pour lire le contenu du fichier (quel dÃ©limiteur ?)
    #     pour chaque ligne
    #         ajouter au dictionnaire une paire clÃ©-valeur
    #         la clÃ© est construite avec une information contenue dans la ligne
    #         la valeur est le namedtuple Station dont les champs sont contenus dans la ligne
    with open('stations-meteo.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for ligne in reader:
            d[ligne['Station']] = Station(ligne['Trafic'], ligne['Rang'], ligne['Ville'])
            
            
    
    return d

if __name__ == '__main__':
    # votre code de test ici...
    d = build_hist_dict('trafic-annuel-entrant-par-station-du-reseau-ferre-2016.csv')
    print(d['GARE DE LYON'])
    print(d['NOISY-CHAMPS'])
    print(d['GARE DE LYON'].Trafic)
    print(d['NOISY-CHAMPS'].Rang)
    print(d['NOISY-CHAMPS'].Ville)
    print('Writing JSON...')
    with open('trafic-annuel-entrant-par-station-du-reseau-ferre-2016', 'w') as jsonfile:
        json.dump(d, jsonfile)
    print('Done !')