from unittest.mock import patch, MagicMock
from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
import sys
from ..lifx_block import Lifx


class TestLifx(NIOBlockTestCase):

    def test_block(self):
        with patch(Lifx.__module__ + '.Light') as mock_light:
            blk = Lifx()
            self.configure_block(blk, {"mac": 'a2:b3:c4:d5',
                                       "ip": '12.12.12.12'})
            blk.start()
            blk.process_signals([Signal({"power": 1,
                                         "hue": 350,
                                         "sat": 3500,
                                         "bri": 3553})])
            blk.stop()
            self.assert_num_signals_notified(1)
            self.assertDictEqual(
                self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                {"power": 1,
                 "hue": 350,
                 "sat": 3500,
                 "bri": 3553})
