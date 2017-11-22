# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:58:03 2017

@author: romain
"""

import csv, json
from collections import namedtuple

def build_dict(csvfile):
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
    # CrÃ©er un dictionnaire vide pour stocker les donnÃ©es
    d = dict()
    # ouvrir le fichier csv
    # utiliser un objet DictReader pour lire le contenu du fichier (quel dÃ©limiteur ?)
    #     pour chaque ligne
    #         ajouter au dictionnaire une paire clÃ©-valeur
    #         la clÃ© est construite avec une information contenue dans la ligne
    #         la valeur est le namedtuple Station dont les champs sont contenus dans la ligne
    with open('./2016.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for ligne in reader:
            d[ligne['Station']] = Station(ligne['Trafic'], ligne['Rang'], ligne['Ville'])
            
            
    
    return d

if __name__ == '__main__':
    # votre code de test ici...
    d = build_dict('./2016.csv')
    print(d['GARE DE LYON'])
    print(d['NOISY-CHAMPS'])
    print(d['GARE DE LYON'].Trafic)
    print(d['NOISY-CHAMPS'].Rang)
    print(d['NOISY-CHAMPS'].Ville)
    print('Writing JSON...')
    with open('trafic-annuel-entrant-par-station-du-reseau-ferre-2016', 'w') as jsonfile:
        json.dump(d, jsonfile)
    print('Done !')
