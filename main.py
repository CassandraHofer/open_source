# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:13:15 2017

@author: lanciar
"""

import numpy as np # import package
import matplotlib.pyplot as plt # import module

x = np.random.randn(10000)

b = list(range(-4,5,1))
n, bins, patches = plt.hist(x, bins=b)

plt.xlabel('bins')
plt.ylabel('count')
plt.title('10.000 random numbers')

plt.show()