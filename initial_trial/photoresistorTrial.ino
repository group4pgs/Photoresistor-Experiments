//This file gives the instantaneous voltage values provided by the photoresistor every second in the Serial O/P

int photoPin = 11; //The photoresistor is connected to the Pin11 to get Analog input
void setup() {
  Serial.begin(9600); 
  pinMode(photoPin,INPUT);
}

void loop() {
  int light = analogRead(photoPin);
  Serial.println(light);
  delay(1000); // Wait for a second
}
