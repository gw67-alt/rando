const int analogPin = A0; // Pin where the analog signal is connected
int analogValue = 0;      // Variable to store the analog value
int mappedValue = 0;      // Variable to store the mapped value

void setup() {
  Serial.begin(9600); // Initialize serial communication at 9600 bits per second
}

void loop() {
  randomSeed(analogRead(analogPin)); // Seed the random number generator with a noise value from the analog pin

  
  Serial.println("1"); // Print the mapped value to the serial monitor
  
  delay(random(50, 2500)); // Wait for a random time between 50 and 150 milliseconds before the next loop
}