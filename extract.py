# encoding: utf8
"""
Created on Tue Nov 21 21:58:03 2017

@author: Cassandra Hofer & Romain Lancia
"""

import csv
from collections import namedtuple


class Extract:
    
    def __init__(self, csvfile):
        self.csvfile = csvfile
        
        
    def build_dict_trafic(self):
        """
        génere un dictionnaire des différentes stations de transports en commun du fichier csv de l'objet courant
    
        Returns:
            dictionnaire de namedtuple des informations relatives aux stations de transports en commun
            
        >>> d = ext.Extract('csv/2016.csv').build_dict_trafic()
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
        """
        génere la liste des trafics des différentes stations de transport en commun du fichier csv de l'objet courant

        Returns:
            Liste des trafics relatives aux stations de transports en commun

        >>> l = ext.Extract('csv/2016.csv').get_trafic()
        [36352115, 18340798, 11462253, 10899310, 8792715, 8351649, 7381123, 6992609, 6889717, 7063687, 6290697, 6133119, 5896554, 6013067, 5178469, 5245603, 5036297, 5126473, 5157761, 5317006, 4994071, 4305206, 4307422, 3829404, 3977748, 4020524, 4010100, 4179663, 3661072, 3803232, 3616052, 3769284, 3509866, 3575805, 3346731, 3151413, 3134776, 3078947, 2979524, 2975436, 3094974, 2870252, 2794182, 2729376, 2475539, 2423494, 2316136, 2388835, 2279221, 2196535, 2139259, 2037263, 1906906, 1812544, 1831297, 1608558, 1597696, 1429509, 1523465, 1366605, 958552, 642202, 564032, 352513, 37192652, 8989578, 8404924, 4462976, 3552088, 3343757, 2151853, 585494, 17491541, 10981914, 9024733, 8381433, 8432306, 2664077, 6815851, 6865612, 5891713, 6080322, 6164559, 4966081, 5070872, 4300906, 4647724, 4656048, 4103831, 4192585, 3895615, 3648085, 3520605, 3363265, 3335906, 2850830, 3281669, 2863984, 3172612, 3550425, 3102623, 3021317, 2872445, 2745396, 2820580, 2782782, 2663534, 2569940, 2529256, 2672036, 2405459, 2694704, 2430271, 2297351, 2223888, 2096180, 2495811, 2070907, 1925980, 1871202, 1773665, 1725103, 1690807, 1679432, 1466310, 1501598, 1281234, 742869, 671787, 618124, 172812, 6407808, 5755055, 6183873, 5000661, 3823443, 2482050, 2007606, 1115170, 974338, 45879586, 30359225, 16128080, 15031139, 11402348, 10317385, 10145616, 9438016, 10856026, 7356084, 7737626, 7095196, 7089241, 6175537, 5890665, 6158849, 5847907, 6099638, 5589061, 5765809, 5025588, 5085421, 4923871, 4944020, 4980193, 4315153, 4551649, 4344027, 4139059, 4282997, 4145014, 4143606, 3985487, 3905952, 3928197, 3767032, 3356879, 3289639, 3410557, 2544008, 2833439, 3082105, 3009210, 3131944, 2971998, 2946177, 3140382, 2769540, 2622025, 2255703, 2391609, 2276012, 2314720, 2226802, 2260458, 2187883, 2044451, 2006980, 1929011, 1738843, 1755560, 1513782, 884202, 360890, 22934672, 7355560, 5499946, 5157016, 4171797, 3564563, 3609052, 3461601, 2298313, 2122393, 1248923, 923579, 451954, 50872319, 20373189, 13225099, 11764439, 9621986, 8000496, 7274236, 7335865, 6630341, 6063343, 5879264, 5533112, 5581700, 5316753, 5311324, 5080418, 4857996, 4547754, 4587665, 4311908, 4348973, 4195883, 4279661, 4070093, 3794787, 3667554, 3645866, 3685441, 3528982, 3512664, 3367371, 3202618, 2965420, 2669794, 2885201, 2641580, 2626600, 2561884, 3201707, 2432844, 2380218, 2341763, 2178463, 2110789, 2366043, 2085927, 1929562, 1814488, 1688254, 1710231, 1642759, 1466777, 1270793, 1233216, 1239904, 739282, 47738502, 31115228, 12969924, 6911244, 4868790, 4454977, 4141694, 4094800, 3384237, 3158806, 2987714, 2704755, 2681812, 2554932, 2431429, 2198203, 2209283, 2165738, 1860491, 1806210, 816797, 766786, 714901, 708085, 611015, 13466536, 9083545, 7932555, 7562865, 6945565, 7103304, 6643601, 7058223, 7963672, 5884810, 5895561, 5740806, 5859214, 5544847, 5207485, 5215902, 4875315, 4903776, 4808099, 4786149, 4706560, 4619691, 4701323, 3899198, 3835814, 3802054, 3725695, 3577070, 3519746, 3598231, 3415341, 3486870, 3383369, 3094950, 2853699, 3105469, 2879755, 2817908, 2760380, 2574219, 2579124, 2419456, 2260212, 2342747, 2243672, 2323166, 2304258, 2109969, 2093279, 2151353, 2074698, 1963737, 1300317, 1558885, 1445627, 1313242, 1249446, 1218261, 980057, 521634, 26356131, 7862183, 6718268, 5390454, 4501642, 2125885, 1600341, 1028405, 923888, 706968, 610753]
        """ 
        lst_trafic = []
        stations = self.build_dict_trafic()
        for station in stations.keys():
            lst_trafic.append((int)(stations[station].Trafic))      
        return lst_trafic

    def build_dict_accessibilite(self):
        """
        génere un dictionnaire des différentes stations de transport en commun du fichier csv de l'objet courant

        Returns:
        dictionnaire de namedtuple des informations relatives aux stations de transports en commun

        >>> d = ext.Extract('csv/access.csv').build_dict_accessibilite()
        >>> print(d['Gare de Lyon'])
        nomptar(Accessibilite='1', lat=48.8446521102, long=2.37310814421)
        >>> print(d['Noisy-Champs'])
        nomptar(Accessibilite='4', lat=48.8426610663, long=2.57825244785)
        >>> print(d['Gare de Lyon'].Accessibilite)
        1
        >>> print("{}, {}".format(d['Noisy-Champs'].lat, d['Noisy-Champs'].long))
        48.8426610663, 2.57825244785
        """
        
        Station = namedtuple('nomptar', ['Accessibilite', 'lat', 'long'])
        # Crée un dictionnaire vide pour stocker les données
        d = dict()
        # pour chaque ligne on ajoute au dictionnaire une paire clé-valeur
        # la clé est construite avec une information contenue dans la ligne
        # la valeur est le namedtuple Station dont les champs sont contenus dans la ligne
        with open(self.csvfile) as f:
            reader = csv.DictReader(f, delimiter=';')
            for ligne in reader:
                # remplacement des caractere spéciaux contenus dans les fichiers csv
                key = ligne['nomptar']
                key = key.replace('Ã©', 'é')
                key = key.replace('Ã¨', 'è')
                key = key.replace('Ã¢', 'â')
                key = key.replace('Ã´', 'ô')
                key = key.replace('Ã§', 'ç')
                lat, long = ligne['coord'].split(', ')
                d[key] = Station(ligne['Accessibilite Quai Train'], (float)(lat), (float)(long))
        return d
    
    def get_accessibilite(self):
        """
        génere la liste des accessibilités des différentes stations de transport en commun du fichier csv de l'objet courant
        
        Returns:
            Liste des accessibilités relatives aux stations de transports en commun

        >>> l = ext.Extract('csv/access.csv').get_trafic()
        [0, 4, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 1, 4, 4, 4, 1, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 4, 4, 4, 1, 1, 4, 1, 1, 4, 4, 4, 4, 0, 0, 0, 0, 1, 0, 4, 4, 4, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0]
        """
        lst_accessibilite = []
        stations = self.build_dict_accessibilite()
        for station in stations.keys():
            lst_accessibilite.append((int)(stations[station].Accessibilite))

        print(lst_accessibilite)
        return lst_accessibilite
