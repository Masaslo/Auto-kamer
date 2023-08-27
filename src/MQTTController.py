import paho.mqtt.client as mqtt

class MqttController:
    def __init__(self, broker_address, port=1883):
        self.broker_address = broker_address
        self.port = port
        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f"connected with result code {rc}")

    def on_message(self, client, userdata, message):
        data = message.payload.decode()
        print(f"Recived message on topic '{message.topic}': \n '{data}'\n")

    def connect(self):
        self.client.username_pw_set("boersfm", "P6Kv9Kakc5VcGPBu6FVr")
        self.client.connect(self.broker_address, self.port)
        self.client.loop_start()

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

if __name__ == "__main__":
    mqtt_controller = MqttController("mqtt.hva-robots.nl")
    mqtt_controller.connect()
    mqtt_controller.subscribe("boersfm/thuis/#")

    try:
        while True:
            # Your main application code here
            pass
    except KeyboardInterrupt:
        mqtt_controller.disconnect()