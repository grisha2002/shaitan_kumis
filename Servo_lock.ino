#include<Servo.h>
#define BUZZER_PIN 7

void peep()
{
  tone(BUZZER_PIN, 4000, 5000);
}

Servo ser;
int poser = 0;
void setup() {
  pinMode(10, OUTPUT);
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Input 1 to Turn LED on and 2 to off, Enter 3 to rotate, Enter 4 to rotate backwards, Enter 5 to turn on the buzzer, ^ to turn of the buzer");
  ser.attach(9);
}
void loop() {
  if (Serial.available())
  {
    /*int state = Serial.parseInt();
      if (state == 1)
      {
      digitalWrite(10, HIGH);
      Serial.println("Command completed LED turned ON");
      }
      if (state == 2)
      {
      digitalWrite(10, LOW);
      Serial.println("Command completed LED turned OFF");
      }
      if (state == 3)
      {
      poser = 0;
      ser.write(poser);
      delay(40);
      }
      if (state == 4)
      {
      poser = 90;
      ser.write(poser);
      delay(40);
      }
      if (state == 5);
      {
      peep();
      }
      if (state == 6);
      {
      tone(BUZZER_PIN, 0, 100)
      }*/
    char command = Serial.read();
    switch (command)
    {
      case '1':
      {
        digitalWrite(10, HIGH);
      Serial.println("Command completed LED turned ON");
      }
      break;
      case '2':
      {
      digitalWrite(10, LOW);
      Serial.println("Command completed LED turned OFF");
      }  
      break;

      case '3':
       {
      poser = 0;
      ser.write(poser);
      delay(40);
      }                
      break;
      case '4':
       {
      poser = 90;
      ser.write(poser);
      delay(40);
      }
      break;
      case '5':
          {
      peep();
      }      
      break;
      case '6':
      {
      tone(BUZZER_PIN, 0, 100);
      }
      break;
    }
  }
}
