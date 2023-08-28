import sys
import time
import paho.mqtt.client as mqtt
import serial
from SerialControllerModule import SerialController
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
        # try:
        #     last_push = pushBulletObjectInClass.get_push_from_index(0)
        #     if(last_push.get("title") == "AK - Mqtt Disconnected"):
        #         self.pushBulletObjectInClass.dismiss_push(pushes_list.get(""))
        # except PushBulletException:
        #     pass

    def on_disconnect(self, client, userdata, flags, rc):
        DISCONNECTED_MESSAGE = f"disconnecten from MQTT server {self.broker_address} as with result code {rc}.\nUser data: {userdata}"
        print(DISCONNECTED_MESSAGE)
        pushBulletObjectInClass.send_notification("AK - Mqtt Disconnected", DISCONNECTED_MESSAGE)



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

def check_message(topic, message, serialObjectInFunction, pushBulletObjectInFunction):
    try:
        if topic == "boersfm/thuis/licht":
            if message == "aan":
                print("trying to turn light on")
                serialObjectInFunction.sendDataToSerial("lichtAan")
            elif message == "uit":
                print("trying to turn light off")
                serialObjectInFunction.sendDataToSerial("lichtUit")
        if topic == "boersfm/thuis/exit":
            systemExit(pushBulletObjectInFunction, "System exit via MQTT command. Message :\n" + message)
        print("message processed\n")
    except Exception as exception:
        print("failed to send message, error:")
        print(exception)

def systemExit(pushBulletObjectInFunction, message):
    time.sleep(1)
    pushBulletObjectInFunction.send_notification("AK - System Exit", message)
    time.sleep(1)
    sys.exit(0)

if __name__ == "__main__":
    try:
        # make a pushBulletController instance
        pushBulletController = PushBulletController()

        # Try connecting to AMC0 and if that fails connect to ACM1, else serialCOntroller is set to null
        try:
            print("connecting to /dev/ttyACM0 as a serial device")
            serialController = SerialController('/dev/ttyACM0', 9600)

        except serial.serialutil.SerialException:
            try:
                print("connecting to /dev/ttyACM0 as a serial device failed")
                print("connecting to /dev/ttyACM1 as a serial device")
                serialController = SerialController('/dev/ttyACM1', 9600)

            except serial.serialutil.SerialException:
                serialController = None
                print("connecting to arduino failed again, please ")


        mqttController = MqttController(MQTT_BROKER, serialController, pushBulletController)
        mqttController.connect()

        while True:
            try:
                serial_data = serialController.readFromSerial()
                if serial_data:
                    print("serial data recieved: " + serial_data)
                    if(serial_data == 10 or serial_data == "10"):
                        # sys.exit(1)
                        pass
                time.sleep(.05)
            except Exception as e:
                systemExit(pushBulletController, "Error:\n" + str(e))
    except KeyboardInterrupt:
        pass