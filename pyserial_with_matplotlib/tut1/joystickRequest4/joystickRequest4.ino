int Xpin = A0, Ypin = A1, Spin = 2, dt = 0;
int Xval, Yval, Sval;
char userInput;

void setup() {
	// put your setup code here, to run once:
	Serial.begin(115200);
	pinMode(Xpin, INPUT);
	pinMode(Ypin, INPUT);
	pinMode(Spin, INPUT);
	digitalWrite(Spin, 1);
}

int* printJoystickVal() {
	Xval = analogRead(Xpin);
	Yval = map(analogRead(Ypin), 0, 1023, 1023, 0);
	Sval = digitalRead(Spin);
	
	delay(dt);
    Serial.print(Xval);
    Serial.print(",");
    Serial.print(Yval);
    Serial.print(",");
    Serial.println(Sval);
}

void loop() {
	// put your main code here, to run repeatedly:
	if(Serial.available() > 0) {
		userInput = Serial.read();		
		if(userInput == 'y') {
            printJoystickVal();
		}
	}
}
