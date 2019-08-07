
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.finance as mpf

start = (2014, 5, 1)
end = (2014, 6, 30)

quotes = mpf.quotes_historical_yahoo('^GDAXI', start, end)

print(quotes)

plt.show()

