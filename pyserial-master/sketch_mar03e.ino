#include <SimpleDHT.h>

int pinDHT11 = 9; // el pin donde envio datos 
SimpleDHT11 dht11(pinDHT11);

void setup() {
  Serial.begin(115200);
  
}
void loop() {
  // start working...
  //Serial.println("=================================");
  //Serial.println("Sample DHT11...");
  
  // read without samples.
  byte temperature = 0;
  byte humidity = 0;
  int err = SimpleDHTErrSuccess;
  if ((err = dht11.read(&temperature, &humidity, NULL))
  != SimpleDHTErrSuccess) {
    Serial.print("Read DHT11 failed, err="); 
    Serial.println(err);delay(1000);
    return;
  }
  
  Serial.print("Sample OK: ");
  Serial.print((int)temperature); Serial.print(" *C, "); 
  Serial.print((int)humidity);Serial.println(" H");
  
  // DHT11 sampling rate is 1HZ.
  delay(1500);
}


