from unittest.mock import patch, MagicMock
from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
import sys


from ..lifx_block import Lifx


class TestLifx(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        sys.modules['lifxlan'] = MagicMock()
        from ..lifx_block import Lifx
        global Lifx

    def test_process_signals(self):
        """Signals pass through block unmodified."""
        with patch(Lifx.__module__ + '.LifxLAN') as mock_lan:
            blk = Lifx()
            self.configure_block(blk, {})
            blk.start()
            blk.process_signals([Signal({"hello": "nio"})])
            blk.stop()
            self.assert_num_signals_notified(1)
            self.assertDictEqual(
                self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                {"hello": "nio"})
