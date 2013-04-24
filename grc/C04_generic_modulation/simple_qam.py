#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Simple QAM Simulation
# Author: Joary Paulo
# Description: Simulation of a QAM Transmission using Squared pulse shaping.
# Generated: Wed Apr 24 16:34:35 2013
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
import PyQt4.Qwt5 as Qwt
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
		self.pam_constellation = pam_constellation = [complex(2*i - (constellation_cardinality)+1,0) for i in range(constellation_cardinality)]
		self.pam_constellation_object = pam_constellation_object = digital.constellation_rect(pam_constellation, [], 0, len(pam_constellation), 1, 2, 0)
		self.constellation_type = constellation_type = 'psk' # 'pam', 'qam' or 'psk'
		self.sps = sps = 32
		self.snr_db = snr_db = 5
		self.const_object = const_object = pam_constellation_object if constellation_type == 'pam' else constellations()[constellation_type](constellation_cardinality)
		self.snr_after_filter = snr_after_filter = snr_db + 10*log10(sps)
		self.samp_rate = samp_rate = 250000
		self.noise_amp = noise_amp = sqrt(  (10**(-snr_db/10.))  /2. )
		self.constellation_power = constellation_power = sqrt(sum([abs(i)**2 for i in const_object.points()])/constellation_cardinality)

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
		self._snr_db_layout = Qt.QVBoxLayout()
		self._snr_db_tool_bar = Qt.QToolBar(self)
		self._snr_db_layout.addWidget(self._snr_db_tool_bar)
		self._snr_db_tool_bar.addWidget(Qt.QLabel("SNR - Sinal to Noise Ratio"+": "))
		self._snr_db_counter = Qwt.QwtCounter()
		self._snr_db_counter.setRange(-20, 60, .1)
		self._snr_db_counter.setNumButtons(2)
		self._snr_db_counter.setValue(self.snr_db)
		self._snr_db_tool_bar.addWidget(self._snr_db_counter)
		self._snr_db_counter.valueChanged.connect(self.set_snr_db)
		self._snr_db_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
		self._snr_db_slider.setRange(-20, 60, .1)
		self._snr_db_slider.setValue(self.snr_db)
		self._snr_db_slider.setMinimumWidth(200)
		self._snr_db_slider.valueChanged.connect(self.set_snr_db)
		self._snr_db_layout.addWidget(self._snr_db_slider)
		self.top_grid_layout.addLayout(self._snr_db_layout, 0,0,10,100)
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
		self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((const_object.points()), 1)
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
		self.connect((self.gr_descrambler_bb_0, 0), (self.blks2_error_rate_0, 1))
		self.connect((self.gr_vector_source_x_0_0, 0), (self.blks2_error_rate_0, 0))
		self.connect((self.blks2_error_rate_0, 0), (self.gr_nlog10_ff_0, 0))
		self.connect((self.gr_nlog10_ff_0, 0), (self.qtgui_time_sink_x_0, 0))

	def get_constellation_cardinality(self):
		return self.constellation_cardinality

	def set_constellation_cardinality(self, constellation_cardinality):
		self.constellation_cardinality = constellation_cardinality
		self.set_pam_constellation([complex(2*i - (self.constellation_cardinality)+1,0) for i in range(self.constellation_cardinality)])
		self.set_const_object(self.pam_constellation_object if self.constellation_type == 'pam' else constellations()[self.constellation_type](self.constellation_cardinality))
		self.set_constellation_power(sqrt(sum([abs(i)**2 for i in self.const_object.points()])/self.constellation_cardinality))

	def get_pam_constellation(self):
		return self.pam_constellation

	def set_pam_constellation(self, pam_constellation):
		self.pam_constellation = pam_constellation
		self.set_pam_constellation_object(digital.constellation_rect(self.pam_constellation, [], 0, len(self.pam_constellation), 1, 2, 0))

	def get_pam_constellation_object(self):
		return self.pam_constellation_object

	def set_pam_constellation_object(self, pam_constellation_object):
		self.pam_constellation_object = pam_constellation_object
		self.set_const_object(self.pam_constellation_object if self.constellation_type == 'pam' else constellations()[self.constellation_type](self.constellation_cardinality))

	def get_constellation_type(self):
		return self.constellation_type

	def set_constellation_type(self, constellation_type):
		self.constellation_type = constellation_type
		self.set_const_object(self.pam_constellation_object if self.constellation_type == 'pam' else constellations()[self.constellation_type](self.constellation_cardinality))

	def get_sps(self):
		return self.sps

	def set_sps(self, sps):
		self.sps = sps
		self.set_snr_after_filter(self.snr_db + 10*log10(self.sps))

	def get_snr_db(self):
		return self.snr_db

	def set_snr_db(self, snr_db):
		self.snr_db = snr_db
		self._snr_db_counter.setValue(self.snr_db)
		self._snr_db_slider.setValue(self.snr_db)
		self.set_noise_amp(sqrt(  (10**(-self.snr_db/10.))  /2. ))
		self.set_snr_after_filter(self.snr_db + 10*log10(self.sps))

	def get_const_object(self):
		return self.const_object

	def set_const_object(self, const_object):
		self.const_object = const_object
		self.set_constellation_power(sqrt(sum([abs(i)**2 for i in self.const_object.points()])/self.constellation_cardinality))

	def get_snr_after_filter(self):
		return self.snr_after_filter

	def set_snr_after_filter(self, snr_after_filter):
		self.snr_after_filter = snr_after_filter

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.qtgui_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)
		self.qtgui_sink_x_0_1.set_frequency_range(0, self.samp_rate)
		self.qtgui_sink_x_0_1_0.set_frequency_range(0, self.samp_rate)
		self.qtgui_sink_x_0_1_0_0.set_frequency_range(0, self.samp_rate)
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

