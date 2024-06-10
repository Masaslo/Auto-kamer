package com.example.auto_kamer_app;

import android.util.Log;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class MqttHandeler {
    private static final String BROKER_URL = "tcp://mqtt.hva-robots.nl:1883";
    private static final String CLIENT_ID = "auto-kamer-app";
    private static final String TOPIC_PREFIX = "row04/app/";
    private static final String USERNAME = "boersfm";
    private static final String PASSWORD = "P6Kv9Kakc5VcGPBu6FVr";
    private static final String[] TOPICS = {"boersfm/#"};
    private static MqttConnectOptions connectOptions;
    private static MqttClient client;

    static {
        try {
            MemoryPersistence persistence = new MemoryPersistence();
            client = new MqttClient(BROKER_URL, CLIENT_ID, persistence);
            connectOptions = new MqttConnectOptions();
            connectOptions.setUserName(USERNAME);
            connectOptions.setPassword(PASSWORD.toCharArray());
            connectOptions.setKeepAliveInterval(0); // Keep alive timer 0 = no disconnect
            connectOptions.setCleanSession(true);
            connectOptions.setAutomaticReconnect(true);
            connectOptions.setCleanSession(true);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

    public static void connect() {
        try {
            // Connect to the broker
            client.connect(connectOptions);
            Log.d("MQTT", "MQTT connected? " + client.isConnected());
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

    public static boolean isConnected(){
        return client.isConnected();
    }
    public static void publish(String topic, String message) {
        Log.d("MqttHandler", "Publishing Topic: " + topic + " Message: " + message);
        try {
            MqttMessage mqttMessage = new MqttMessage(message.toLowerCase().getBytes());
            client.publish(topic, mqttMessage);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }
}
