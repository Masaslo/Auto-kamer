import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

time.sleep(2)


ser.timeout = 2  # Set a timeout for readline()
ser.readline()   # Read and discard any initial data

try:
    while True:
        # Read a line of data from the serial port and call the callback function
        ser.write(b"lichtAan\n")

        data = ser.readline().decode().strip()  # Read and decode data
        if data:
            print(data)
except KeyboardInterrupt:
    pass

# Close the serial connection when done
ser.close()