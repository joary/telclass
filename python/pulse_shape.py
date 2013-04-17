from numpy import arange, array, pi, sin
from pylab import *
from matplotlib import pyplot as p
from cmath import phase

###################################################
# TODO:
#
#   Make Sinc filter work
#   Make rrc filter work
#   Create Windowing
###################################################

def gen(sample_rate, samp_per_sym, rolloff, filter_size, ptype='square', plot=False):
    ''' Generates the pulse shaping vector to be used by generic_modulator.grc
        sample_rate - simulation sample rate
        samp_per_sym - number of samples per symbol.
        ptype - type of 
    '''


    if ptype == 'square':
        filt = gen_square(samp_per_sym)
    elif ptype == 'sinc':
        filter_size = int(4./rolloff)
        cutoff = 1./(2*samp_per_sym)
        filt = gen_sinc(filter_size, cutoff)
    elif ptype == 'rc':
        filt = gen_rc(filter_size, samp_per_sym, rolloff, plot)
    elif ptype == 'rrc':
        filt = gen_rrc(filter_size, samp_per_sym, rolloff, plot)
    else:
        exit(0) # TODO find a way to show error on GNU Radio Companion

    if plot:
        p.show()

    threshold = 1e-13
    ret = [ 0 if abs(i) < threshold else i for i in filt]

    return ret

def gen_square(filter_size, plot=False):
    ''' Generates Square pulse shapping
        sps - number of samples per symbol.
        ptype - type of 
    '''
    t = arange(-1, 1, 1/(filter_size/2.))
    n = arange(-filter_size/2, filter_size/2)

    filt = [1]*(filter_size)
    filt_freq = array(abs(fftshift(fft(filt))))

    if plot:
        p.figure(1)
        p.subplot(211)
        p.plot(n, filt)
        p.subplot(212)
        p.plot(t, abs(filt_freq), '-o')

    return filt

def gen_hamming_win(size):
#   Comments:
#       4-how the window function will change the filter?
#       TODO

    alpha = 0.54
    beta = 1-alpha
    n = arange(size)/(size-1.)

    win = alpha - beta*cos(2.*pi*n)
    return win

def gen_sinc(filter_size, filter_bw, plot=False):
#   Comments:
#       1-how to calcultate sinc filter?
#           n = [-filter_size/2, filter_size/2]
#           sinc(n) = 2*BW*(sin(2*pi*BW*n))/(2*pi*BW*n)
#       2-what means BW?
#           in frequency domain:
#               BW can be seen as the cutoff frequency, or the pulse 
#               bandwidth, since the filter is real the total bandwith is 
#               2*BW, because of negative mirror
#           in time domain:
#               the maximum representable frequency is Fs/2, using a oversam-
#               pling fatctor L (sps), the maximun usable frequency would
#               be Fs/(2*sps), in this case we can calculate BW with this
#               normalizing the frequency Bw = 1/(2*sps)
#       3-how to choose the filter size?
#           the filter size, influence in rooloff factor (how much frequency
#           filter takes to cut off frequency), we can use the following
#           equation to calculate it: filter_size = 4/rooloff_factor
#           since rooloff_factor = [0, 0.5]
#       4-how the window function will change the filter?
#           See gen_hamming_win() comments
#

    t = arange(-0.5, 0.5 + 1./filter_size, 1./filter_size)
    n = arange(-filter_size/2, filter_size/2+1)
    window = gen_hamming_win(filter_size+1)
  
    # Generate filter 
    filt =  2*filter_bw*sinc(2*filter_bw*n)
    # Normalize filter
    filt_energy = sum(abs(filt)**2)
    filt = filt/sqrt(filt_energy)
    # windowing
    filt = filt*window
    # Generate filter frequency response
    filt_freq = array(abs(fftshift(fft(filt))))

    if plot:
        p.figure(1)
        p.subplot(211)
        p.plot(n, filt, '-o')
        p.subplot(212)
        p.plot(t, abs(filt_freq), '-o')
        p.axis([-0.5, 0.5, 0, 2])
        #p.subplot(222)
        #p.plot(t, phase(filt_freq))
        #p.axis([-1, 1, -pi-1, pi+1])
        #p.subplot(224)
        #p.plot(grp)

    return filt

def gen_rc(filter_size, sps, rolloff, plot = False):
#   Comments:
#       1-how to calcultate raised cossine filter?
#           n = [-filter_size/2, filter_size/2]
#
    t = arange(-0.5, 0.5 + 1./filter_size, 1./filter_size)
    n = arange(-filter_size/2., filter_size/2.+1)

    vsinc = sinc(1.0*n/sps)
    vcos = cos(pi*rolloff*n/sps)
    vdiv = 1 - (4.*(rolloff**2.)*(n**2.))/(sps**2.)
    filt = vsinc*vcos/vdiv
    # Normalize filter
    filt_energy = sum(abs(filt)**2)
    filt = filt/sqrt(filt_energy)
    #print filt_energy
    #filt_energy = sum(abs(filt)**2)
    #print filt_energy
    # windowing
    filt_freq = array(abs(fftshift(fft(filt))))

    if plot:
        p.figure(1)
        p.subplot(211)
        p.plot(n, filt, '-o')
        p.subplot(212)
        p.plot(t, abs(filt_freq), '-o')
        #p.axis([-0.5, 0.5, 0, 2])
        #p.subplot(222)
        #p.plot(t, phase(filt_freq))
        #p.axis([-1, 1, -pi-1, pi+1])
        #p.subplot(224)
        #p.plot(grp)

    return filt

def gen_rrc(filter_size, sps, rolloff, plot = False):
#   Comments:
#       1-how to calcultate raised cossine filter?
#           n = [-filter_size/2, filter_size/2]
#

    filt = gen_rc(filter_size, sps, rolloff)

    print filt

    ret = copysign(sqrt(abs(filt)), filt)

    return ret


