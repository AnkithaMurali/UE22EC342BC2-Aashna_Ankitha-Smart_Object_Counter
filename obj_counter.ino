#define IR_SENSOR_PIN 2
#define MOTOR_IN1 4
#define MOTOR_IN2 5

int objectCount = 0;
bool detected = false;

void setup() {
  pinMode(IR_SENSOR_PIN, INPUT);
  pinMode(MOTOR_IN1, OUTPUT);
  pinMode(MOTOR_IN2, OUTPUT);
  Serial.begin(9600);
  moveForward();
}

void loop() {
  int sensorVal = digitalRead(IR_SENSOR_PIN);

  if (sensorVal == LOW && !detected) {
    objectCount++;
    detected = true;
    Serial.print("Object Count: ");
    Serial.println(objectCount);
  }

  if (sensorVal == HIGH) {
    detected = false;
  }

  delay(50);
}

void moveForward() {
  digitalWrite(MOTOR_IN1, HIGH);
  digitalWrite(MOTOR_IN2, LOW);
}
