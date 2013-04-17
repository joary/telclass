#!/usr/bin/python

from pylab import *
import constellation as c
from matplotlib import pyplot as p
import random as r
import pulse_shape as f
from gnuradio import gr

def simulate(M=4, num_syms=10, sps=8, pulse_type='square'):

    samp_rate = 1
    bps = log2(M)
    const = c.constellation(M, 'qam');
    #pulse = f.gen(2500, sps, 0.35, 10*11*sps, pulse_type)
    
    rolloff = 0.1
    pulse = gr.firdes.low_pass(1, 1, 1.0/sps, rolloff)

    print pulse
    #############################
    # Logs
    #############################

    N0 = int(len(pulse)-1)
    
    print "#############################"
    print "Pulse Len:", len(pulse)
    print "N0:", N0
    print "#############################"


    #############################
    # Transmitter
    #############################

    # Create Symbol Chunks
    tx_chunks = array([r.choice(range(M)) for i in range(num_syms)])
    # Create Symbols
    tx_syms = const.vec[tx_chunks]
    # Upsampling
    tx_upsamp = zeros(num_syms*sps - (sps-1), dtype=complex)
    tx_upsamp[::sps] = tx_syms
    # Filtering with pulse shape
    tx_sig = convolve(tx_upsamp, pulse)
    #tx_sig = tx_sig[0:num_syms*sps]

    #############################
    # Channel
    #############################

    rx_sig = tx_sig

    #############################
    # Receiver
    #############################
    # Flip Left-Right
    pulse = pulse[::-1]

    # Qual a diferenca de descontar N0 antes da convolucao de depois?
    rx_filtered = convolve(rx_sig, pulse)
    rx_sym = rx_filtered[N0:N0+num_syms*sps:sps]

    #rx_filtered = rx_sig
    #rx_sym = rx_filtered[:-1:sps]

  
    #############################
    # Plots 
    #############################

    syms_to_plot = 400
    sig_to_plot = syms_to_plot*sps
    plot_upsampling = False
    plot_syms = True
    plot_sig = False
    plot_pulse = True

    p.figure()
    p.subplot(211)
    vec = convolve(pulse, pulse)
    p.stem(range(len(vec)), vec)
    p.subplot(212)
    p.plot(abs(fftshift(fft(vec))))
    

    if plot_upsampling:
        p.figure()
        p.plot(real(tx_upsamp[0:sig_to_plot]), '-o')
        p.plot(imag(tx_upsamp[0:sig_to_plot]), '-o')
        p.xlabel("Upsampled Symbols")

    if plot_pulse:
        p.figure()
        p.subplot(211)
        p.stem(range(len(pulse)), pulse)
        p.subplot(212)
        p.plot(abs(fftshift(fft(pulse))))
        p.xlabel("Pulse Shape")

    if plot_sig:
        p.figure()
        p.subplot(211)
        p.plot(real(tx_sig[:sig_to_plot]), '-o')
        p.plot(imag(tx_sig[:sig_to_plot]), '-o')
        p.xlabel("Transmitted Signal")
        p.subplot(212)
        p.plot(real(rx_filtered[:sig_to_plot]), '-o')
        p.plot(imag(rx_filtered[:sig_to_plot]), '-o')
        p.xlabel("Matched Filtered Signal")

    if plot_syms:
        p.figure()
        p.subplot(211)
        #p.stem(range(syms_to_plot), real(stream_sym[0:syms_to_plot]), markerfmt='bo')
        #p.stem(range(syms_to_plot), imag(stream_sym[0:syms_to_plot]), markerfmt='ro')a
        p.plot(real(tx_syms[0:syms_to_plot]), '-o')
        p.plot(imag(tx_syms[0:syms_to_plot]), '-o')
        p.xlabel("Transmitted Symbols")
        p.subplot(212)
        #p.stem(range(syms_to_plot), real(rx_sym[0:syms_to_plot]), markerfmt='bo')
        #p.stem(range(syms_to_plot), imag(rx_sym[0:syms_to_plot]), markerfmt='ro')
        p.plot(real(rx_sym[0:syms_to_plot]), '-o')
        p.plot(imag(rx_sym[0:syms_to_plot]), '-o')
        p.xlabel("Received Symbols")

    p.show()

if __name__ == '__main__':
    simulate(4, 1000, 8, 'rc')

