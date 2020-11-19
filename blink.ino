int let = 13;

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
