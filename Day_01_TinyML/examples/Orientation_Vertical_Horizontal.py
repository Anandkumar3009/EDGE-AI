# read IMU data and print it on the serial terminal

import time
from lsm6dsox import LSM6DSOX
from machine import Pin, SPI

# Initialize SPI for Nicla Vision
# SPI(5) is the internal bus, PF6 is the CS pin for the IMU
spi = SPI(5)
cs = Pin("PF6", Pin.OUT_PP, Pin.PULL_UP)
lsm = LSM6DSOX(spi, cs)

print("Ax,Ay,Az,Gx,Gy,Gz")


while(True):
    a = lsm.accel()  # a[0]=X, a[1]=Y, a[2]=Z
    g = lsm.gyro()
    # Thresholding: We check which axis is feeling the most gravity (~9.8)
    # Using a range (e.g., > 8) is safer than checking for exactly 9.8
    print("%f, %f, %f, %f, %f, %f" % (
    a[0], a[1], a[2],
    g[0], g[1], g[2]))

    if abs(a[2]) > 0.8:
        print("Horizontal (Lying Flat)")
    elif abs(a[1]) > 0.8:
        print("Vertical (Standing Up - Portrait)")
    elif abs(a[0]) > 0.8:
        print("Vertical (Standing Up - Landscape)")
    else:
        print("Random Alignment")

    time.sleep_ms(500)
