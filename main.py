# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:06:13 2017

@author: hoferc
"""
import numpy as np

import histogramme as histo

def main():
    w = np.random.randn(10000)
    x = np.random.randn(10000)
    y = np.random.randn(10000)
    z = np.random.randn(10000)

    b = list(range(-4,5,1))

    histogramme = histo.Histogramme(w, x, y, z, b, "bins", "count", "10.000 random numbers")
    histogramme.afficherHistogramme()
                                         

    


if __name__ == "__main__":
    main()