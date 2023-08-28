import paho.mqtt.client as mqtt
from main import writeToSerial

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        # Subscribe to the desired topic here
        client.subscribe("boersfm/thuis/#")  # Replace with the topic you want to subscribe to
    else:
        print(f"Connection failed with code {rc}")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    topic = msg.topic
    message = str(msg.payload)
    print(topic+" "+message)
    if(topic == "boersfm/thuis/licht"):
        if(message == "b'aan'"):
            print("licht gaat nu aan")
            writeToSerial("lichtAan")

def send_message(topic, message):
    result = client.publish(topic, message)
    status = result[0]
    if status == 0:
        print(f"sent `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

username = "boersfm"  # Replace with your MQTT broker username
password = "P6Kv9Kakc5VcGPBu6FVr"  # Replace with your MQTT broker password


broker_address = "mqtt.hva-robots.nl"  # Replace with the address of your MQTT broker
port = 1883  # Replace with the port of your MQTT broker

# Set the username and password for authentication
client.username_pw_set(username, password)
client.connect(broker_address, port, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()