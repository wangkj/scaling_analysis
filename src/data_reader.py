import datetime

import pandas.io.data as web
from scipy.fftpack import fft
import matplotlib.pyplot as plt
SAN = 'SAN.MC'

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
f=web.DataReader(SAN, 'yahoo', start, end)
plt.plot(f.Close)
ft_t = fft(f.Close)
ft_minus_t = [ft_t[len(ft_t)-j].conjugate() for j in range(len(ft_t),0, -1)]
print len(ft_minus_t)
print (len(ft_t))
plt.plot((1.0/len(f))*(ft_t*ft_minus_t))
plt.show()
