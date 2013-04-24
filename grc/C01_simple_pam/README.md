# PAM simulation

# About the simulation:
This simulation modulate bits using PAM constelattion,
adds Wight Gaussian Noise to generated symbols
and demodulate symbols with treshold detection.

A Scrambler of bits were used to make symbols have equal probability
of happen.

open the simulation with:

    #> gnuradio-companion simple_pam.grc

run the simulation with:

    F6

# About the parameters

## User defined parameters

### Transmitter/Receiver

* *samp_rate:* the sample rate of the simulation, also called the sampling frequency (in samples per second or, as some people prefer, Hz)

* *sps:* the oversampling factor, i. e., the number of samples per symbol

* *constellation_cardinality (M):*  number of symbols in constellation vector
the number of bits per constellaiton symbol can be seen as log2(M)

### Channel

* *snr_db*: signal to noise decibel level.

## Automaticaly calculated parameters

* *constellation:* Constellation vector calculated with python as:

    [complex(2*i - (constellation_cardinality)+1,0) for i in range(constellation_cardinality)]

for constellation_cardinality = 4, the result is:

    [(-3+0j), (-1+0j), (1+0j), (3+0j)]

* *constellation_power:* Constellation power calculated with python as:

    sqrt(sum(abs(array(constellation))**2)/constellation_cardinality)

for constellation_cardinality = 4, the result is:

    2.2360679774997898

* *const_object:* Object necessary for demodulation block, defines demodulation
behavior, created with python as:

    gnuradio.digital.constellation_rect(constellation, pre_diff_code, rotational_symmetry, real_sectors, imag_sectors, width_real_sectors, width_imag_sectors)

especificaly for PAM, we use:
    pre_diff_code = []
    rotational_symmetry = 0
    real_sectors = len(constellation)
    imag_sectors = 0
    width_real_sectors = 2
    width_imag_sectors = 0

see: http://gnuradio.org/doc/sphinx/digital/constellations.html

* *noise_amp:* Noise amplitude calculated based on signal to noise decibel level
using the folowing python code

    sqrt(  (10**(-snr_db/10.))  /2. )

