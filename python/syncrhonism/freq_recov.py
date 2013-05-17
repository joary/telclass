#!/usr/bin/python

from pylab import *
from matplotlib import pyplot as p
#from cmath import phase

def phase(a):
    return arctan2(imag(a), real(a))

def recov():
    # get this file on http://www.laps.ufpa.br/joary/tuto/rx_from_usrp.32fc
    rx = fromfile(open('rx_from_usrp.32fc'), dtype=complex64)

    fsync_init = 6104 #2824
    fsync_end = fsync_init + 1024 - 4

    freq_sync = array(rx[fsync_init:fsync_end])

    data_init = fsync_end
    data_end = data_init + 2000

    data = array(rx[data_init:data_end])
    phase_v = [ phase(i) for i in freq_sync]

    phase_diff = [abs(phase(freq_sync[i] * conj(freq_sync[i+1]))) for i in range(len(freq_sync)-1)]

    freq_correction = mean(phase_diff)
    recov_factor = pi/2 - freq_correction
    print recov_factor

    freq_recov = [ freq_sync[i]*exp(complex(0, i*recov_factor)) for i in range(len(freq_sync))]

    data_recov = [ data[i]*exp(complex(0,i*recov_factor)) for i in range(len(data))]

    end = None
    p.figure()
    p.subplot(212)
    p.plot([pi/2 - i for i in phase_diff[:end]])
    p.plot([recov_factor]*len(phase_diff[:end]))
    p.xlabel("Phase Differenc")
    p.subplot(211)
    p.plot(phase_v[:end])
    p.xlabel("Phase")

#   #diff = freq_sync[:-1] * conj(freq_sync[1:])
#   #phase_diff = [phase(i) for i in diff]
    p.figure()
    p.subplot(211)
    p.plot(real(freq_sync), '-ob')
    p.plot(imag(freq_sync), '-or')
    p.xlabel("Frequency Recovery Sequence")
    p.subplot(212)
    p.plot(real(freq_recov), '-ob')
    p.plot(imag(freq_recov), '-or')
    p.xlabel("Frequency Correction")

    p.figure()
    p.subplot(211)
    p.plot(real(data_recov), '-ob')
    p.plot(imag(data_recov), '-or')
    p.subplot(212)
    p.plot(real(data_recov), imag(data_recov), 'o')
    p.xlabel("Data Correction")

    p.show()

if __name__ == '__main__':
    recov()

