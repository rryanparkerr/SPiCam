#include "SleepyPi2.h"
#include <Time.h>
#include <LowPower.h>
#include <PCF8523.h>
#include <Wire.h>

int led = 13;

void setup() {
	pinMode(led, OUTPUT);
	SleepyPi.enablePiPower(true);
}

void loop() {
	digitalWrite(led, HIGH);
	delay(1000);
	digitalWrite(led, LOW);
        delay(1000);	
}
