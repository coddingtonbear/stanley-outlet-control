#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Stanley Tx
# Generated: Wed Dec 23 13:15:34 2015
# NOTE: Altered significantly from generated form!
#       See `stanley_tx.py` for original!
##################################################

from gnuradio import blocks
from gnuradio import gr
from argparse import ArgumentParser
import osmosdr


OUTLETS = {
    '1': {
        'off': '1001101001101001101001101001001101101001001001101001101001001001001001001',  # noqa
        'on': '1001101001101001101001101001001101101001001001101001101001001001001101101',  # noqa
    },
    '2': {
        'off': '1001101001101001101001101101101001001001001001101001101001001001001001001',  # noqa
        'on': '1001101001101001101001101101101001001001001001101001101001001101101001001',  # noqa
    },
    '3': {
        'off': '1001101001101001101001101001001001001101101001101001101001001001001001001',  # noqa
        'on': '1001101001101001101001101001001001001101101001101001101101101001001001001',  # noqa
    }
}


class StanleyController(gr.top_block):
    def __init__(self, vector):
        gr.top_block.__init__(self, "Stanley Tx")

        ##################################################
        # Variables
        ##################################################
        self.interp = interp = 1200
        self.baud_rate = baud_rate = 1872
        self.samp_rate = samp_rate = baud_rate*interp
        self.center_freq = center_freq = 433893000

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_sink_0 = osmosdr.sink(args="numchan=" + str(1) + " " + "")
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(center_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(14, 0)
        self.osmosdr_sink_0.set_if_gain(40, 0)
        self.osmosdr_sink_0.set_bb_gain(40, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(2000000, 0)

        self.blocks_vector_source_x_0 = blocks.vector_source_c(
            (([int(v) for v in vector] + [0]*25) * 100), False, 1, []
        )
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, interp)
        self.blocks_moving_average_xx_0 = blocks.moving_average_cc(
            20, 0.9/20, 4000
        )

        ##################################################
        # Connections
        ##################################################
        self.connect(
            (self.blocks_moving_average_xx_0, 0), (self.osmosdr_sink_0, 0)
        )
        self.connect(
            (self.blocks_repeat_0, 0), (self.blocks_moving_average_xx_0, 0)
        )
        self.connect(
            (self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0, 0)
        )

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp
        self.set_samp_rate(self.baud_rate*self.interp)

    def get_baud_rate(self):
        return self.baud_rate

    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate
        self.set_samp_rate(self.baud_rate*self.interp)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_sink_0.set_center_freq(self.center_freq, 0)


def main():
    parser = ArgumentParser()
    parser.add_argument('outlet_number', choices=OUTLETS.keys())
    parser.add_argument('set_to', choices=('on', 'off'))
    args = parser.parse_args()

    vector = OUTLETS[args.outlet_number][args.set_to]

    tb = StanleyController(vector)
    tb.start()
    tb.wait()
