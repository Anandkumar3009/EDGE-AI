# This work is licensed under the MIT license.
# Copyright (c) 2013-2023 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# Blinky example


"""
import time
from machine import LED

led = LED("LED_BLUE")

while True:
    led.on()
    time.sleep_ms(500)
    led.off()
    time.sleep_ms(1000)
"""

# Different colours

import time
from machine import LED

led_red = LED("LED_RED")
led_blue = LED("LED_BLUE")

while True:
    led_red.on()
    time.sleep_ms(500)
    led_red.off()
    led_blue.on()
    time.sleep_ms(1000)
    led_blue.off()
