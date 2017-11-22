# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:05:30 2017

@author: hoferc
"""
import urllib

class Telechargement():
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.chargement()
        
    def chargement(self):
        # lancement du téléchargement
        proxy_address = 'http://147.215.1.189:3128/'
        proxy_handler = urllib.request.ProxyHandler({'http': proxy_address, 'https': proxy_address})
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(self.source, self.destination)
        print ("Telechargement du fichier {} à l'emplacement {}".format(self.source, self.destination))
        