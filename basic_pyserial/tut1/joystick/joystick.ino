int Xpin = A0, Ypin = A1, Spin = 2, dt = 300;
int Xval, Yval, Sval;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(Xpin, INPUT);
  pinMode(Ypin, INPUT);
  pinMode(Spin, INPUT);
  digitalWrite(Spin, 1);
}

void loop() {
  // put your main code here, to run repeatedly:
  Xval = analogRead(Xpin);
  Yval = analogRead(Ypin);
  Sval = digitalRead(Spin);
  
  delay(dt);
  
  Serial.print("Xval = ");
  Serial.print(Xval);
  Serial.print(" | ");
  
  Serial.print("Yval = ");
  Serial.print(Yval);
  Serial.print(" | ");

  Serial.print("Sval = ");
  Serial.print(Sval);
  Serial.println(" | ");

}
