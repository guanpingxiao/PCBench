import numpy as np
data = np.loadtxt('data.txt',  float, ndmin=2, delimiter=',', max_rows=100, unpack=True, like=None, comments='#', encoding='utf-8', converters=None, skiprows=2, usecols=(0, 1))
