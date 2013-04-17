# PAM/QAM/PSK simulation

# About the simulation:
open the simulation with:
    gnuradio-companion simple_pam.grc
run the simulation with:
    F6

# About the parameters
* *samp_rate:* the sample rate of simulation, it changes how fast the simulation treat samples.

* *sps:* Number of samples per modulation symbol, 

* *constellation_cardinality (M):*  number of symbols in constellation vector
the number of bits per constellaiton symbol can be seen as log2(M)

* *constellation_type:* type of modulation being used: "qam", "pam" or "psk"

* *snr_db*: signal to noise decibel level.

* *all the other parameters are automaticaly calculated*
