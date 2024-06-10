package com.example.auto_kamer_app;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.navigation.fragment.NavHostFragment;

import com.example.auto_kamer_app.databinding.FragmentFirstBinding;

public class FirstFragment extends Fragment {

    private FragmentFirstBinding binding;
    @Override
    public View onCreateView(
            @NonNull LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState
    ) {

        binding = FragmentFirstBinding.inflate(inflater, container, false);
        return binding.getRoot();

    }

    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        Log.d("MQTT", "BABA ");

        binding.buttonOn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(!MqttHandeler.isConnected()){
                    MqttHandeler.connect();
                }
                Log.d("MqttHandler", "CLICKED ON");
                MqttHandeler.publish("boersfm/lights", "true");
            }
        });
        binding.buttonOff.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(!MqttHandeler.isConnected()){
                    MqttHandeler.connect();
                }
                Log.d("MqttHandler", "CLICKED ON");
                MqttHandeler.publish("boersfm/lights", "false");
            }
        });

    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }

}