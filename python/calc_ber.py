#!/usr/bin/python

from pylab import *
from matplotlib import pyplot as p

import sys

def calc_snr(plot = False):
    tx = fromfile(open('tx_sym.32fc'), dtype=complex64)
    rx = fromfile(open('rx_sym.32fc'), dtype=complex64)

    if (len(tx) == 0 or len(rx) == 0):
        print 'Not valid data'
        print '\tPlease run gnuradio simulation first'
        exit(-1)

    size = min([len(tx), len(rx)]) - 1
    rx = rx[0:size]
    tx = tx[0:size]

    tx_power = sum([abs(tx[i])**2 for i in range(size)])
    rx_power = sum([abs(rx[i])**2 for i in range(size)])
    noise_power = sum([abs(tx[i] - rx[i])**2 for i in range(size)])

    SNR = 1.0*tx_power/noise_power
    SNR_dB = 10*log10(SNR)

    if plot:
        init = 0
        end = 100
        p.subplot(211)
        p.plot(list(real(tx[init:end])), '-o')
        p.plot(list(imag(tx[init:end])), '-o')
        p.subplot(212)
        p.plot(list(real(rx[init:end])), '-o')
        p.plot(list(imag(rx[init:end])), '-o')
        p.show()

    return SNR_dB

def calc_ber(M):
    bps = int(log2(M))
    tx = fromfile(open('tx.8b'), dtype=byte)
    rx = fromfile(open('rx.8b'), dtype=byte)

    print len(tx), len(rx)

    if (len(tx) == 0 or len(rx) == 0):
        print 'Not valid data'
        print '\tPlease run gnuradio simulation first'
        exit(-1)

    size = min([len(tx), len(rx)])
    rx = rx[0:size]
    tx = tx[0:size]

    #print tx, rx
    bit_errors = 0
    for i in range(size):
        if tx[i] != rx[i]:
            #print i, tx[i], rx[i], bin(tx[i]), bin(rx[i])
            bit_errors += bin(tx[i]^rx[i]).count('1')

    #print bit_errors

    ber = 1.0*bit_errors/(size*bps)
    return ber

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Usage: cal_ber.py M'
        print '\tM - Constellation Order'
        exit(0)

    snr_db = calc_snr()
    ber = calc_ber(int(sys.argv[1]))

    print "BER: ", ber
    print "SNR: ", snr_db
