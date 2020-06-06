int sensorState = 0;

void setup() {
   pinMode(3, INPUT);
   pinMode(13, OUTPUT);
}

void loop() {
   sensorState = digitalRead(2);

   if (sensorState == LOW) {
     digitalWrite(13, LOW);
   }
   else {
      digitalWrite(13, HIGH);
   }
}
