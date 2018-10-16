Lifx
====
nio block for connecting to a Lifx smart bulb on the same network. The MAC address and IP address of the light must be known. Colors are described using hue, saturation, and brightness.

| Color | Hue | Saturation | Brightness |
| ----- | :---: | :---: | :---: | 
| Red | 65535 | 65535 | 65535 |
| Orange | 6500 | 65535 | 65535 |
| Yellow | 9000 | 65535 | 65535 |
| Green | 16000 | 65535 | 65535 |
| Blue | 43000 | 65535 | 65535 |
| White | 58275 | 0 | 65535 |

Properties
----------
- **bri**: Brightness of the bulb, (0-65535) 0 will turn the bulb off.
- **hue**: Hue of the bulb (0-65535).
- **ip**: IP address of the light.
- **kelvin**: Temp of the light in Kelvin (2500-9000).
- **kill_switch**: If selected, light will turn off when nio service stops.
- **mac**: MAC address of the light.
- **power**: Turn the bulb on or off(1 for on 0 for off).
- **sat**: Saturation of the bulb color(0-65535).

Inputs
------
- **default**: Any list of Signals.

Outputs
-------
- **default**: The same list of signals.

Requirements
------------
lifxlan

Commands
--------
None

