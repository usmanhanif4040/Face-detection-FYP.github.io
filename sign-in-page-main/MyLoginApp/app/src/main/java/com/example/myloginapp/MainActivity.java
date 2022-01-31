package com.example.myloginapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        TextView username =(TextView) findViewById(R.id.username);
        TextView Password =(TextView) findViewById(R.id.Password);

        MaterialButton loginbtn = (MaterialButton) findViewById(R.id.loginbtn)

                //admin and admin
        loginbtn.setOnClickListener(new View.OnClickListener(){

            public void OnClick(View v){
                if(username.gettext().tostring().equals("admin") && password.getText().tostring().equals("admin")

                Toast.makeText(MainActivity.this, "Login Successfull", Toast.LENGTH_SHORT).show();
                )else
                Toast.makeText(MainActivity.this, "Login Failed", Toast.LENGTH_SHORT).show();
            }

        })





        })
    }
}
