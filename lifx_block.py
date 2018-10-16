from nio.block.base import Block
from nio.properties import VersionProperty, IntProperty, \
                           BoolProperty, StringProperty
import sys
from lifxlan import Light


class Lifx(Block):

    version = VersionProperty('0.1.0')
    mac = StringProperty(title='MAC address', default='[[LIFX_MAC]]')
    ip = StringProperty(title='IP Address', default='[[LIFX_IP]]')
    power = IntProperty(title='1 for on 0 for off', default=0)
    hue = IntProperty(title='Hue (0-65535)', default=0)
    sat = IntProperty(title='Saturation (0-65535)', default=0)
    bri = IntProperty(title='Brightness (0-65535)', default=65535)
    kelvin = IntProperty(title='Kelvin (2500-9000)', default=3500)
    kill_switch = BoolProperty(title='Turn off Light at Service Stop?',
                               default=True, advanced=True)

    def configure(self, context):
        super().configure(context)
        self.bulb = Light(self.mac(), self.ip())

    def process_signals(self, signals):
        for signal in signals:
            if self.power(signal) == 0:
                brightness = 0
            else:
                brightness = self.bri(signal)
                self.bulb.set_power(True)
            self.bulb.set_color([self.hue(signal),
                                 self.sat(signal),
                                 brightness,
                                 self.kelvin(signal)])
            pass
        self.notify_signals(signals)

    def stop(self):
        if self.kill_switch():
            self.bulb.set_power(False)
        super().stop()
