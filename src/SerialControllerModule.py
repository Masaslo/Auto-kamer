import serial
class SerialController:
    def __init__(self, device, baudrate):
        self.data = None
        self.ser = serial.Serial(device, baudrate)
        self.ser.timeout = 2
    def readFromSerial(self):
        self.data = self.ser.readline().decode().strip()  # Read and decode data
        return self.data
    def sendDataToSerial(self, sending_data):
        print(f"sent: {sending_data} to Serial device")
        encoded_string = f"{sending_data}\n".encode('utf-8')
        self.ser.write(encoded_string)