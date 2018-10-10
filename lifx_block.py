from nio.block.base import Block
from nio.properties import VersionProperty, IntProperty, BoolProperty
import sys
from lifxlan import LifxLAN


class Lifx(Block):

    version = VersionProperty('0.1.0')
    power = IntProperty(title='1 for on 0 for off', default=0)
    hue = IntProperty(title='Hue (0-65535)', default=0)
    sat = IntProperty(title='Saturation (0-65535)', default=0)
    bri = IntProperty(title='Brightness (0-65535)', default=65535)
    kelvin = IntProperty(title='Kelvin (2500-9000)', default=3500)

    def configure(self, context):
        super().configure(context)
        lan = LifxLAN()
        devices = lan.get_lights()
        self.bulb = devices[0]

    def process_signals(self, signals):
        for signal in signals:
            if self.power(signal) == 0:
                brightness = 0
            else:
                brightness = self.bri(signal)
            self.bulb.set_color([self.hue(signal),
                                 self.sat(signal),
                                 brightness,
                                 self.kelvin(signal)])
            pass
        self.notify_signals(signals)

    def stop(self):
        self.bulb.set_power(False)
        super().stop()
