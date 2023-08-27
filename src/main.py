# import MQTTConnection as connection
import time
import serial
import paho.mqtt.client as mqtt
from pushBulletModule import PushBulletController

MQTT_BROKER = "mqtt.hva-robots.nl"

MQTT_ID = "AutoKamer_V1"
MQTT_USR_NAME = "boersfm"
MQTT_USR_PASS = "P6Kv9Kakc5VcGPBu6FVr"

class MqttController:
    def __init__(self, BROKER_ADDRESS, serialObject, pushBulletObject, port=1883):
        self.broker_address = BROKER_ADDRESS
        self.port = port
        self.client = mqtt.Client(MQTT_ID)
        self.serialObjectInClass = serialObject
        self.pushBulletObjectInClass = pushBulletObject

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f"connected to MQTT server {self.broker_address} as with result code {rc}")
        self.client.subscribe("boersfm/thuis/#")

    def on_message(self, client, userdata, message):
        message_data = message.payload.decode()
        print(f"Recived message on topic '{message.topic}': \n'{message_data}'\nnow attempting to decode")
        check_message(message.topic, message_data, self.serialObjectInClass, self.pushBulletObjectInClass)

    def connect(self):
        self.client.username_pw_set(MQTT_USR_NAME, MQTT_USR_PASS)
        self.client.connect(self.broker_address, self.port)
        self.client.loop_start()

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

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

def check_message(topic, message, serialObjectInFunction, pushBulletObjectInFunction):
    try:
        if topic == "boersfm/thuis/licht":
            if message == "aan":
                print("trying to turn light on")
                serialObjectInFunction.sendDataToSerial("lichtAan")
            elif message == "uit":
                print("trying to turn light off")
                serialObjectInFunction.sendDataToSerial("lichtUit")
        print("message processed\n")
    except Exception as e:
        print("failed to send message, error:")
        print(e)


if __name__ == "__main__":
    try:
        # make a pushBulletController instance
        pushBulletController = PushBulletController()

        # Try connecting to AMC0 and if that fails connect to ACM1, else serialCOntroller is set to null
        try:
            print("connecting to /dev/ttyACM0 as a serial device")
            serialController = SerialController('/dev/ttyACM1', 9600)

        except serial.serialutil.SerialException:
            try:
                print("connecting to /dev/ttyACM0 as a serial device failed")
                print("connecting to /dev/ttyACM1 as a serial device")
                serialController = SerialController('/dev/ttyACM1', 9600)

            except serial.serialutil.SerialException:
                serialController = null
                print("connecting to arduino failed again, please ")


        mqttController = MqttController(MQTT_BROKER, serialController, pushBulletController)
        mqttController.connect()

        while True:
            serial_data = serialController.readFromSerial()
            if serial_data:
                print(serial_data)
            time.sleep(.05)
    except KeyboardInterrupt:
        pass

# Close the serial connection when done
