int Xpin = A0, Ypin = A1, Spin = 2, dt = 0;
int Xval, Yval, Sval;
unsigned long previousTime = 0, currentTime = 0;
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
	Yval = analogRead(Ypin);
	Sval = digitalRead(Spin);
	
	delay(dt);
    Serial.print(Xval);
    Serial.print(",");
    Serial.print(Yval);
    Serial.print(",");
    Serial.print(Sval);
}

void loop() {
	// put your main code here, to run repeatedly:
	if(Serial.available() > 0) {
		userInput = Serial.read();		
		if(userInput == 'g') {
            printJoystickVal();
		}

        else if(userInput == 'c') {
            previousTime = currentTime;
            currentTime = millis();

            printJoystickVal();
            Serial.print(",");
			Serial.print(currentTime - previousTime);
        }
	}
}
