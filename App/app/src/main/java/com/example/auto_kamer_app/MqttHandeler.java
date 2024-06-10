package com.example.auto_kamer_app;

import android.app.Activity;
import android.util.Log;

import org.eclipse.paho.client.mqttv3.MqttConnectOptions;

public class MqttHandeler {
    private static final String BROKER_URL = "tcp://82.165.34.5";
    private static final String CLIENT_ID = "auto-kamer-app";
    private static final String TOPIC_PREFIX = "row04/app/";
    private static final String USERNAME = "boersfm";
    private static final String PASSWORD = "";
    private MqttConnectOptions connectOptions;
}
