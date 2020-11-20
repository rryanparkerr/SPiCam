#include "SleepyPi2.h"
#include <Time.h>
#include <LowPower.h>
#include <PCF8523.h>
#include <Wire.h>

int led = 13;

void setup() {
	pinmode(led, OUTPUT);
	SleepyPi.enablePiPower(true);
}

void loop() {
	digitalWrite(let, HIGH);
	delay(1000);
	digitalWrite(let, LOW);
        delay(1000);	
}
