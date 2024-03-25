#include <ESP32Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

int degree= 40;

void setup() {
  // Initialize the serial communication
  Serial.begin(9600);

  // Attach the servos to corresponding pins
  servo1.attach(21); 
  servo2.attach(22); 
  servo3.attach(19);
  servo4.attach(23);
  servo5.attach(18);
  servo6.attach(5);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    // Perform actions based on the received command
    switch (command) {
      case '0':
        servo2.write(degree);  
        servo4.write(degree);  
        servo5.write(degree);  
        delay(1000);       
        servo2.write(-degree);
        servo4.write(-degree);
        servo5.write(-degree);   
        Serial.println("0 is printed");
        break;
      
      case '1':
        servo1.write(degree);  
        delay(1000);       
        servo1.write(-degree);   
        break;

      case '2':
        servo1.write(degree);
        servo2.write(degree);
        delay(1000);
        servo1.write(-degree);
        servo2.write(-degree);
        break;

      case '3':
        servo1.write(degree);
        servo4.write(degree);
        delay(1000);
        servo1.write(-degree);
        servo4.write(-degree);
        break;

      case '4':
        servo1.write(degree);
        servo4.write(degree);
        servo5.write(degree);
        delay(1000);
        servo1.write(-degree);
        servo4.write(-degree);
        servo5.write(-degree);
        break;

      case '5':
        servo1.write(degree);
        servo5.write(degree);
        delay(1000);
        servo1.write(-degree);
        servo5.write(-degree);
        break;

      case '6':
        servo1.write(degree);
        servo4.write(degree);
        servo2.write(degree);
        delay(1000);
        servo1.write(-degree);
        servo4.write(-degree);
        servo2.write(-degree);
        break;

      case '7':
        servo1.write(degree);
        servo2.write(degree);
        servo4.write(degree);
        servo5.write(degree);
        delay(1000);
        servo1.write(-degree);
        servo2.write(-degree);
        servo4.write(-degree);
        servo5.write(-degree);
        break;

      case '8':
        servo1.write(degree);
        servo5.write(degree);
        servo2.write(degree);
        delay(1000);
        servo1.write(-degree);
        servo5.write(-degree);
        servo2.write(-degree);
        break;

      case '9':
        servo4.write(degree);
        servo2.write(degree);
        delay(1000);
        servo4.write(-degree);
        servo2.write(-degree);
        break;
        
      default:
        // Turn off all servos or perform other actions for default case
        break;
    }
  }
}
