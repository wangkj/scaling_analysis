import numpy as np
from scipy.fftpack import fft

class SpectralDensity(object):

    def __init__(self, signal):
        self.signal = signal

    def _fft(self, signal):
        y = fft(signal)
        print y
        y_minus = []
        print y[len(y)-len(y)].conjugate()
        print y_minus


if __name__ == '__main__':
    dens = SpectralDensity(np.arange(8))
    dens._fft(dens.signal)
        
