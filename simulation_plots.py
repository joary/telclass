from pylab import *
import sys

def signal(init = 0, end = 1000): 
    tx = fromfile(open('tx_sig.32fc'), dtype=complex64)
    rx = fromfile(open('rx_sig.32fc'), dtype=complex64)

    figure()
    subplot(211)
    plot(real(tx[init: end]))
    plot(imag(tx[init: end]))
    subplot(212)
    plot(real(rx[init: end]))
    plot(imag(rx[init: end]))

def symbols(init = 0, end = 20): 
    tx = fromfile(open('tx_sym.32fc'), dtype=complex64)
    rx = fromfile(open('rx_sym.32fc'), dtype=complex64)

    figure()
    subplot(221)
    plot(real(tx[init: end]), '-o')
    plot(imag(tx[init: end]), '-o')
    subplot(222)
    plot(real(tx[init: end]), imag(tx[init: end]), 'o')
    axis([2, -2, 2, -2])
    subplot(223)
    plot(real(rx[init: end]), '-o')
    plot(imag(rx[init: end]), '-o')
    subplot(224)
    plot(real(rx[init: end]), imag(rx[init: end]), 'o')
    axis([2, -2, 2, -2])

def compare_signals_symbols(init=0, end=10, sps=128):
    tx_sig = fromfile(open('tx_sig.32fc'), dtype=complex64)
    rx_sig = fromfile(open('rx_sig.32fc'), dtype=complex64)
    tx_sym = fromfile(open('tx_sym.32fc'), dtype=complex64)
    rx_sym = fromfile(open('rx_sym.32fc'), dtype=complex64)

    init_sig = init*sps
    end_sig = end*sps

    figure()
    subplot(221)
    plot(real(tx_sig[init_sig: end_sig]))
    plot(imag(tx_sig[init_sig: end_sig]))
    xlabel("Transmitted Signal")
    subplot(223)
    plot(real(rx_sig[init_sig: end_sig]))
    plot(imag(rx_sig[init_sig: end_sig]))
    xlabel("Received Signal")
    subplot(222)
    plot(real(tx_sym[init: end]), '-o')
    plot(imag(tx_sym[init: end]), '-o')
    xlabel("Transmitted Symbols")
    subplot(224)
    plot(real(rx_sym[init: end]), '-o')
    plot(imag(rx_sym[init: end]), '-o')
    xlabel("Received Symbols")





