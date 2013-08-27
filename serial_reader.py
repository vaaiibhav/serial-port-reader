import sys
import serial

port = "/dev/ttyS0"
baud = 9600

sread = serial.Serial()
sread.port = port
sread.baudrate = baud

try:
    sread.open()
except:
    sys.stderr.write("Error opening serial port %s\n" % (sread.portstr) )
    sys.exit(1)

sread.setRtsCts(0)

while 1:
  # Read from serial port, blocking
    data = sread.read(1)

    # If there is more than 1 byte, read the rest
    n = sread.inWaiting()
    if n:
        data = data + sread.read(n)

    sys.stdout.write(data)
