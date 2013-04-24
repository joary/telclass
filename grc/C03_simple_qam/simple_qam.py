#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Simple QAM Simulation
# Author: Joary Paulo
# Description: Simulation of a QAM Transmission using Squared pulse shaping.
# Generated: Wed Apr 24 16:23:22 2013
##################################################

from PyQt4 import Qt
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.digital.modulation_utils import type_1_constellations as constellations
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.qtgui import qtgui
from grc_gnuradio import blks2 as grc_blks2
from math import sqrt, sin, pi
from numpy import log2, array, arange, log10
from optparse import OptionParser
import sip
import sys

class simple_qam(gr.top_block, Qt.QWidget):

	def __init__(self):
		gr.top_block.__init__(self, "Simple QAM Simulation")
		Qt.QWidget.__init__(self)
		self.setWindowTitle("Simple QAM Simulation")
		self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
		self.top_scroll_layout = Qt.QVBoxLayout()
		self.setLayout(self.top_scroll_layout)
		self.top_scroll = Qt.QScrollArea()
		self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
		self.top_scroll_layout.addWidget(self.top_scroll)
		self.top_scroll.setWidgetResizable(True)
		self.top_widget = Qt.QWidget()
		self.top_scroll.setWidget(self.top_widget)
		self.top_layout = Qt.QVBoxLayout(self.top_widget)
		self.top_grid_layout = Qt.QGridLayout()
		self.top_layout.addLayout(self.top_grid_layout)


		##################################################
		# Variables
		##################################################
		self.constellation_cardinality = constellation_cardinality = 16
		self.const_object = const_object = constellations()['qam'](constellation_cardinality)
		self.snr_db = snr_db = 20
		self.constellation = constellation = const_object.points()
		self.sps = sps = 8
		self.samp_rate = samp_rate = 250000
		self.noise_amp = noise_amp = sqrt(  (10**(-snr_db/10.))  /2. )
		self.constellation_power = constellation_power = sqrt(sum([abs(i)**2 for i in constellation])/constellation_cardinality)

		##################################################
		# Blocks
		##################################################
		self.tabid_0 = Qt.QTabWidget()
		self.tabid_0_widget_0 = Qt.QWidget()
		self.tabid_0_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabid_0_widget_0)
		self.tabid_0_grid_layout_0 = Qt.QGridLayout()
		self.tabid_0_layout_0.addLayout(self.tabid_0_grid_layout_0)
		self.tabid_0.addTab(self.tabid_0_widget_0, "TX")
		self.tabid_0_widget_1 = Qt.QWidget()
		self.tabid_0_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabid_0_widget_1)
		self.tabid_0_grid_layout_1 = Qt.QGridLayout()
		self.tabid_0_layout_1.addLayout(self.tabid_0_grid_layout_1)
		self.tabid_0.addTab(self.tabid_0_widget_1, "CHANNEL")
		self.tabid_0_widget_2 = Qt.QWidget()
		self.tabid_0_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabid_0_widget_2)
		self.tabid_0_grid_layout_2 = Qt.QGridLayout()
		self.tabid_0_layout_2.addLayout(self.tabid_0_grid_layout_2)
		self.tabid_0.addTab(self.tabid_0_widget_2, "RX")
		self.top_grid_layout.addWidget(self.tabid_0, 30,0,10,100)
		self.tabid_2 = Qt.QTabWidget()
		self.tabid_2_widget_0 = Qt.QWidget()
		self.tabid_2_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabid_2_widget_0)
		self.tabid_2_grid_layout_0 = Qt.QGridLayout()
		self.tabid_2_layout_0.addLayout(self.tabid_2_grid_layout_0)
		self.tabid_2.addTab(self.tabid_2_widget_0, "symbol-based")
		self.tabid_2_widget_1 = Qt.QWidget()
		self.tabid_2_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabid_2_widget_1)
		self.tabid_2_grid_layout_1 = Qt.QGridLayout()
		self.tabid_2_layout_1.addLayout(self.tabid_2_grid_layout_1)
		self.tabid_2.addTab(self.tabid_2_widget_1, "bit-based")
		self.tabid_2_widget_2 = Qt.QWidget()
		self.tabid_2_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabid_2_widget_2)
		self.tabid_2_grid_layout_2 = Qt.QGridLayout()
		self.tabid_2_layout_2.addLayout(self.tabid_2_grid_layout_2)
		self.tabid_2.addTab(self.tabid_2_widget_2, "BER")
		self.tabid_0_layout_2.addWidget(self.tabid_2)
		self.tabid_1 = Qt.QTabWidget()
		self.tabid_1_widget_0 = Qt.QWidget()
		self.tabid_1_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabid_1_widget_0)
		self.tabid_1_grid_layout_0 = Qt.QGridLayout()
		self.tabid_1_layout_0.addLayout(self.tabid_1_grid_layout_0)
		self.tabid_1.addTab(self.tabid_1_widget_0, "bit-based")
		self.tabid_1_widget_1 = Qt.QWidget()
		self.tabid_1_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabid_1_widget_1)
		self.tabid_1_grid_layout_1 = Qt.QGridLayout()
		self.tabid_1_layout_1.addLayout(self.tabid_1_grid_layout_1)
		self.tabid_1.addTab(self.tabid_1_widget_1, "scrambled")
		self.tabid_1_widget_2 = Qt.QWidget()
		self.tabid_1_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabid_1_widget_2)
		self.tabid_1_grid_layout_2 = Qt.QGridLayout()
		self.tabid_1_layout_2.addLayout(self.tabid_1_grid_layout_2)
		self.tabid_1.addTab(self.tabid_1_widget_2, "symbol-based")
		self.tabid_0_grid_layout_0.addWidget(self.tabid_1, 0,0,10,10)
		self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
			1024, #size
			samp_rate, #bw
			"QT GUI Plot", #name
			1 #number of inputs
		)
		self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
		self.tabid_2_layout_2.addWidget(self._qtgui_time_sink_x_0_win)
		self.qtgui_sink_x_0_1_0_0 = qtgui.sink_f(
			1024, #fftsize
			firdes.WIN_BLACKMAN_hARRIS, #wintype
			0, #fc
			samp_rate, #bw
			"QT GUI Plot", #name
			False, #plotfreq
			False, #plotwaterfall
			True, #plottime
			True, #plotconst
		)
		self._qtgui_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_1_0_0.pyqwidget(), Qt.QWidget)
		self.tabid_1_layout_0.addWidget(self._qtgui_sink_x_0_1_0_0_win)
		self.qtgui_sink_x_0_1_0 = qtgui.sink_f(
			1024, #fftsize
			firdes.WIN_BLACKMAN_hARRIS, #wintype
			0, #fc
			samp_rate, #bw
			"QT GUI Plot", #name
			True, #plotfreq
			False, #plotwaterfall
			True, #plottime
			True, #plotconst
		)
		self._qtgui_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
		self.tabid_1_layout_1.addWidget(self._qtgui_sink_x_0_1_0_win)
		self.qtgui_sink_x_0_1 = qtgui.sink_c(
			1024, #fftsize
			firdes.WIN_BLACKMAN_hARRIS, #wintype
			0, #fc
			samp_rate, #bw
			"QT GUI Plot", #name
			False, #plotfreq
			False, #plotwaterfall
			True, #plottime
			True, #plotconst
		)
		self._qtgui_sink_x_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_1.pyqwidget(), Qt.QWidget)
		self.tabid_1_layout_2.addWidget(self._qtgui_sink_x_0_1_win)
		self.qtgui_sink_x_0_0_0_0 = qtgui.sink_c(
			1024, #fftsize
			firdes.WIN_BLACKMAN_hARRIS, #wintype
			0, #fc
			samp_rate, #bw
			"QT GUI Plot", #name
			True, #plotfreq
			False, #plotwaterfall
			True, #plottime
			True, #plotconst
		)
		self._qtgui_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
		self.tabid_2_layout_0.addWidget(self._qtgui_sink_x_0_0_0_0_win)
		self.qtgui_sink_x_0_0_0 = qtgui.sink_f(
			1024, #fftsize
			firdes.WIN_BLACKMAN_hARRIS, #wintype
			0, #fc
			samp_rate, #bw
			"QT GUI Plot", #name
			False, #plotfreq
			False, #plotwaterfall
			True, #plottime
			True, #plotconst
		)
		self._qtgui_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
		self.tabid_2_layout_1.addWidget(self._qtgui_sink_x_0_0_0_win)
		self.qtgui_sink_x_0_0 = qtgui.sink_c(
			1024, #fftsize
			firdes.WIN_BLACKMAN_hARRIS, #wintype
			0, #fc
			samp_rate, #bw
			"QT GUI Plot", #name
			True, #plotfreq
			False, #plotwaterfall
			True, #plottime
			False, #plotconst
		)
		self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)
		self.tabid_0_layout_1.addWidget(self._qtgui_sink_x_0_0_win)
		self.gr_vector_source_x_0_0 = gr.vector_source_b(([1,0]), True, 1)
		self.gr_vector_source_x_0 = gr.vector_source_b(([1,0]), True, 1)
		self.gr_unpack_k_bits_bb_0 = gr.unpack_k_bits_bb(int(log2(constellation_cardinality)))
		self.gr_throttle_0 = gr.throttle(gr.sizeof_gr_complex*1, samp_rate)
		self.gr_pack_k_bits_bb_0 = gr.pack_k_bits_bb(int(log2(constellation_cardinality)))
		self.gr_null_sink_0 = gr.null_sink(gr.sizeof_char*1)
		self.gr_noise_source_x_0 = gr.noise_source_c(gr.GR_GAUSSIAN, noise_amp, 0)
		self.gr_nlog10_ff_0 = gr.nlog10_ff(1, 1, 0)
		self.gr_multiply_const_vxx_0_0 = gr.multiply_const_vcc((1./constellation_power, ))
		self.gr_multiply_const_vxx_0 = gr.multiply_const_vcc((constellation_power, ))
		self.gr_file_sink_0_1_0 = gr.file_sink(gr.sizeof_gr_complex*1, "rx_sym.32fc")
		self.gr_file_sink_0_1_0.set_unbuffered(False)
		self.gr_file_sink_0_1 = gr.file_sink(gr.sizeof_gr_complex*1, "tx_sym.32fc")
		self.gr_file_sink_0_1.set_unbuffered(False)
		self.gr_file_sink_0_0 = gr.file_sink(gr.sizeof_char*1, "rx.8b")
		self.gr_file_sink_0_0.set_unbuffered(False)
		self.gr_file_sink_0 = gr.file_sink(gr.sizeof_char*1, "tx.8b")
		self.gr_file_sink_0.set_unbuffered(False)
		self.gr_descrambler_bb_0 = gr.descrambler_bb(0xe4001, 0x7ffff, 19)
		self.gr_char_to_float_1_0 = gr.char_to_float(1, 1)
		self.gr_char_to_float_1 = gr.char_to_float(1, 1)
		self.gr_char_to_float_0 = gr.char_to_float(1, 1)
		self.gr_add_xx_0 = gr.add_vcc(1)
		self.digital_scrambler_bb_0 = digital.scrambler_bb(0xe4001, 0x7fffF, 19)
		self.digital_constellation_receiver_cb_0 = digital.constellation_receiver_cb(const_object.base(), 6.28/100, -0.25, +0.25)
		self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((constellation), 1)
		self.blks2_error_rate_0 = grc_blks2.error_rate(
			type='BER',
			win_size=samp_rate,
			bits_per_symbol=1,
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_vector_source_x_0, 0), (self.digital_scrambler_bb_0, 0))
		self.connect((self.digital_scrambler_bb_0, 0), (self.gr_pack_k_bits_bb_0, 0))
		self.connect((self.gr_pack_k_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
		self.connect((self.digital_constellation_receiver_cb_0, 0), (self.gr_file_sink_0_0, 0))
		self.connect((self.digital_constellation_receiver_cb_0, 0), (self.gr_unpack_k_bits_bb_0, 0))
		self.connect((self.gr_unpack_k_bits_bb_0, 0), (self.gr_descrambler_bb_0, 0))
		self.connect((self.gr_descrambler_bb_0, 0), (self.gr_null_sink_0, 0))
		self.connect((self.gr_multiply_const_vxx_0, 0), (self.digital_constellation_receiver_cb_0, 0))
		self.connect((self.gr_descrambler_bb_0, 0), (self.gr_char_to_float_0, 0))
		self.connect((self.gr_char_to_float_0, 0), (self.qtgui_sink_x_0_0_0, 0))
		self.connect((self.gr_add_xx_0, 0), (self.gr_throttle_0, 0))
		self.connect((self.gr_noise_source_x_0, 0), (self.gr_add_xx_0, 1))
		self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.gr_multiply_const_vxx_0_0, 0))
		self.connect((self.gr_multiply_const_vxx_0_0, 0), (self.gr_file_sink_0_1, 0))
		self.connect((self.gr_multiply_const_vxx_0_0, 0), (self.qtgui_sink_x_0_1, 0))
		self.connect((self.gr_char_to_float_1, 0), (self.qtgui_sink_x_0_1_0, 0))
		self.connect((self.gr_pack_k_bits_bb_0, 0), (self.gr_char_to_float_1, 0))
		self.connect((self.gr_pack_k_bits_bb_0, 0), (self.gr_file_sink_0, 0))
		self.connect((self.gr_char_to_float_1_0, 0), (self.qtgui_sink_x_0_1_0_0, 0))
		self.connect((self.gr_vector_source_x_0, 0), (self.gr_char_to_float_1_0, 0))
		self.connect((self.gr_multiply_const_vxx_0_0, 0), (self.gr_add_xx_0, 0))
		self.connect((self.gr_add_xx_0, 0), (self.qtgui_sink_x_0_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.gr_multiply_const_vxx_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.gr_file_sink_0_1_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.qtgui_sink_x_0_0_0_0, 0))
		self.connect((self.gr_nlog10_ff_0, 0), (self.qtgui_time_sink_x_0, 0))
		self.connect((self.blks2_error_rate_0, 0), (self.gr_nlog10_ff_0, 0))
		self.connect((self.gr_vector_source_x_0_0, 0), (self.blks2_error_rate_0, 0))
		self.connect((self.gr_descrambler_bb_0, 0), (self.blks2_error_rate_0, 1))

	def get_constellation_cardinality(self):
		return self.constellation_cardinality

	def set_constellation_cardinality(self, constellation_cardinality):
		self.constellation_cardinality = constellation_cardinality
		self.set_const_object(constellations()['qam'](self.constellation_cardinality))
		self.set_constellation_power(sqrt(sum([abs(i)**2 for i in self.constellation])/self.constellation_cardinality))

	def get_const_object(self):
		return self.const_object

	def set_const_object(self, const_object):
		self.const_object = const_object
		self.set_constellation(self.const_object.points())

	def get_snr_db(self):
		return self.snr_db

	def set_snr_db(self, snr_db):
		self.snr_db = snr_db
		self.set_noise_amp(sqrt(  (10**(-self.snr_db/10.))  /2. ))

	def get_constellation(self):
		return self.constellation

	def set_constellation(self, constellation):
		self.constellation = constellation
		self.set_constellation_power(sqrt(sum([abs(i)**2 for i in self.constellation])/self.constellation_cardinality))

	def get_sps(self):
		return self.sps

	def set_sps(self, sps):
		self.sps = sps

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.qtgui_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)
		self.qtgui_sink_x_0_1_0.set_frequency_range(0, self.samp_rate)
		self.qtgui_sink_x_0_1_0_0.set_frequency_range(0, self.samp_rate)
		self.qtgui_sink_x_0_1.set_frequency_range(0, self.samp_rate)
		self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate)
		self.qtgui_sink_x_0_0_0_0.set_frequency_range(0, self.samp_rate)

	def get_noise_amp(self):
		return self.noise_amp

	def set_noise_amp(self, noise_amp):
		self.noise_amp = noise_amp
		self.gr_noise_source_x_0.set_amplitude(self.noise_amp)

	def get_constellation_power(self):
		return self.constellation_power

	def set_constellation_power(self, constellation_power):
		self.constellation_power = constellation_power
		self.gr_multiply_const_vxx_0_0.set_k((1./self.constellation_power, ))
		self.gr_multiply_const_vxx_0.set_k((self.constellation_power, ))

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	qapp = Qt.QApplication(sys.argv)
	tb = simple_qam()
	tb.start()
	tb.show()
	qapp.exec_()
	tb.stop()

