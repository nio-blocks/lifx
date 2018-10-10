from unittest.mock import patch, MagicMock
from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
import sys
from ..lifx_block import Lifx


class TestLifx(NIOBlockTestCase):

    def test_on(self):
        blk = Lifx()
        self.configure_block(blk, {"power": 1,
                                   "hue": 350,
                                   "sat": 3500,
                                   "bri": 3553})
        blk.start()
        blk.process_signals([Signal({"hello": "nio"})])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {"hello": "nio"})
