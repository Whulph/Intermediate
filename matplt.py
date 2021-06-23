# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:36:07 2021

@author: Tyler
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import lines
import matplotlib



x = np.linspace(0, 5, 10)
y = (x-1.0) ** 2

fig = plt.figure()

# left, bottom, width, height (range 0 to 1)
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # insert axes

# main figure
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')

# insert
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title');