import numpy as np
import pandas as pd

data = np.random.standard_normal((100_0000, 5))
path = '/test/python/'
h5s = pd.HDFStore(path + 'data.h5s', 'w')
h5s['data'] = data
h5s.close()

