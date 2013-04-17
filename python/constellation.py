from numpy import sqrt, real, imag, array, copy
from matplotlib import pyplot as p
from gnuradio import digital

class constellation:
    vec = []
    norm_vec = []
    power = 0
    obj = None

    def __init__(self, M=4, ctype='qam'):
        vec = gen(M, ctype)
        self.vec = copy(vec)
        [self.norm_vec, self.power] = normalize_const(vec)
        self.obj = gen_object(M, ctype)
        

#####################################################################
# TODO: Generate PSK constellation
#####################################################################

def gen(M = 4, ctype='qam', plot=False):
    ''' Generates the constellation matrice to be used by generic_modulator.grc
        M - Constellation number of points
        type - Constellation type ['qam', 'pam', 'psk']
    '''

    if ctype == 'qam':
        const = gen_qam(M, plot)
    elif ctype == 'pam':
        const = gen_pam(M, plot)
    elif ctype == 'psk':
        const = gen_psk(M, plot)
    else:
        exit(0) # TODO find a way to show error on GNU Radio Companion

    return const

def gen_norm(M = 4, ctype='qam'):
    ''' Generate constellation normalized vector
        M - Constellation Number of points
        Type - Constellation Type
    '''

    const = gen(M, ctype)
    [ret, power] = normalize_const(const)
    return ret

def gen_object(M = 4, ctype = 'qam'):
    ''' Generate Constellation decoder object
            it is responsable for demapping received symbols into bits
        M - Constellation Number os points
        Type - Constellation Type
    '''
    const = gen(M, ctype)
    pre_diff = []
    
    if ctype == 'qam':
        obj = digital.constellation_rect(
            const,
            pre_diff, 
            1, # simetry
            int(sqrt(M)), # real constellation size
            int(sqrt(M)), # imag constellation size
            2, # real constellation segment size
            2) # imag constellation segment size
    elif ctype == 'pam':
        obj = digital.constellation_rect(
            const, pre_diff, 0, len(const), 1, 2, 0)
    elif ctype == 'psk':
        obj = None 
        # TODO: implement psk
        exit(0) # TODO find a way to show error on GNU Radio Companion
    else:
        exit(0) # TODO find a way to show error on GNU Radio Companion

    return obj

def gen_pam(M, plot=False):
    ''' Generate PAM Contellation
        M - Constellation Number os points
        plot - Create plot of constellation
    '''
    ret = []
    for i in range(M):
        ret += [complex(2*i-M+1,0)]

    if plot:
        p.plot(real(ret), imag(ret), 'o')
        maxc = M+1
        p.axis([-maxc, maxc, -maxc, maxc])
    
    return array(ret)

def gen_qam(M, plot=False):
    ''' Generate QAM Contellation
        M - Constellation Number os points
        plot - Create plot of constellation
    '''

    # TODO: make it work for non-perfect squares
    M2 = int(sqrt(M))

    ret = []
    for i in range(M2):
        for j in range(M2):
            ret += [complex(2*i-M2+1, 2*j-M2+1)]

    if plot:
        p.plot(real(ret), imag(ret), 'o')
        maxc = M2+1
        p.axis([-maxc, maxc, -maxc, maxc])
    
    return array(ret)

def gen_psk(M, plot=False):
    ''' Generate PSK Contellation
        M - Constellation Number os points
        plot - Create plot of constellation
    '''
    ret = []
    return array(ret)

def normalize_const(vec):
    ''' Normalize constellation vector
        vec - Constellation Vector
    '''
    power = sqrt(sum([abs(i)**2 for i in vec])/(len(vec)))
    vec /= power

    return [vec, power]
    
