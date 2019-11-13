/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
#include "SleepyPi2.h"
#include <Time.h>
#include <LowPower.h>
#include <PCF8523.h>
#include <Wire.h>

int led = 13;
float current = 0.0;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);
  SleepyPi.enablePiPower(true);
  Serial.begin(9600);  
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(led, HIGH);  // turn the LED on (HIGH is the voltage level)
  //Serial.println("On");
  current = SleepyPi.rpiCurrent();
  //Serial.print("mA: ");
  Serial.println(current);
  delay(5000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  //Serial.println("Off");
  delay(5000);               // wait for a second
}
