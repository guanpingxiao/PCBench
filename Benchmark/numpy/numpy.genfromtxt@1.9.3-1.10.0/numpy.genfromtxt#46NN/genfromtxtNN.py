import numpy as np
from io import StringIO
with open('data2.txt', 'rb') as f:
    data = np.genfromtxt(f,  float,  '#',  ',',  0,  0,  0,  None, missing='')
