#!/usr/bin/env python
# 
# Copyright 2013 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from pylab import *
import random
from gnuradio import gr, gr_unittest
import blocks_swig as blocks
from matplotlib import pyplot as p

class qa_data_aided_synchronism_cc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        data_size = 10000
        fb_size = N = 720
        dw=0.01
        SNR=30
        pre_size = 80

        const = array([1j, -1, -1j, 1]) # Constellation
        wc = 2*pi/3 # Carrier frequency
        n = arange(0,N) # #Discrete-time index
   
        pre = array([sqrt(0.5)*complex(randn(), randn()) for i in range(pre_size)])
        data1 = array([random.choice(const) for i in range(data_size)])
        data2 = array([random.choice(const) for i in range(data_size)])
        
        seq = const[ n%4 ]
        s = concatenate([pre, seq, data1, pre, seq, data2]*2)
        tx_carrier = exp(-1j*wc*arange(0, len(s)))
        x = s*tx_carrier
    
        noise = [sqrt((10**(-SNR/10.))/2.)*complex(randn(), randn()) for i in range(len(x))]
        x = x+noise
        
        rx_carrier = exp(1j*(wc+dw)*arange(0, len(s)))
        sq = x*rx_carrier

        print 'ONE', shape(sq)
        
        src = gr.vector_source_c(sq, False)
        prc = blocks.data_aided_synchronism_cc(fb_size, 3., data_size, 10, 10, pre)
        snk = gr.vector_sink_c()

        self.tb.connect(src, prc, snk)
        
        self.tb.run ()

        print "plotting"

        rx = snk.data()
        p.subplot(221)
        #rx_d = sq[len(pre)+len(seq):len(pre)+len(seq)+len(data1)]
        rx_d = sq
        p.plot(real(rx_d), imag(rx_d), 'o')
        p.subplot(222)
        p.plot(real(rx_d), '-o')
        p.plot(imag(rx_d), '-o')
        p.xlabel("Received")
        p.subplot(223)
        #rx = rx[0:len(data1)]
        p.plot(real(rx), imag(rx), 'o')
        p.subplot(224)
        #tx = tx + list(data1)
        p.plot(real(rx), '-o')
        p.plot(imag(rx), '-o')
        p.xlabel("Recovered")
        p.show()

if __name__ == '__main__':
    gr_unittest.run(qa_data_aided_synchronism_cc, "qa_data_aided_synchronism_cc.xml")
