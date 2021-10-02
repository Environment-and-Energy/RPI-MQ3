# boot.py
# Set Circuit Playground Express flash chip to program writeable
#   If toggle switch is right,
#      flash is program writeable and file access is frozen
#   If toggle switch is left,
#      flash chip file access ok, file writes give an error
# via Dan Conley
#   https://learn.adafruit.com/cpu-temperature-logging-with-circuit-python/
#   writing-to-the-filesystem
# 2018 Mike Barela for Getting Started with Circuit Playground Express

import storage
from adafruit_circuitplayground.express import cpx

#storage.unmount("/")
storage.remount("/", cpx.switch)
