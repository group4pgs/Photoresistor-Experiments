int photoPin = 11;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(photoPin,INPUT);
}

void loop() {
  int light = analogRead(photoPin);
  Serial.println(light);
  delay(1000);
}
