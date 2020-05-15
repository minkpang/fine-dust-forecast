
#include "DHT.h"
#include <SDS011-select-serial.h>
#include <SoftwareSerial.h>

#define DHTPIN 2     // what digital pin we're connected to

#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

DHT dht(DHTPIN, DHTTYPE);

float p10,p25;
int error;

SoftwareSerial SDS(3, 4); // RX, TX
SDS011 my_sds(SDS);

void setup() {
  Serial.begin(9600);

  dht.begin();
  SDS.begin(9600);
}

void loop() {

  float h = dht.readHumidity();

  float t = dht.readTemperature();

  if (isnan(h) || isnan(t) ) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  error = my_sds.read(&p25,&p10);
  if (! error) {
    Serial.print("P2.5: ");
    Serial.print(p25);
    Serial.print("\t");
    Serial.print("P10:  ");
    Serial.print(p10);
    Serial.print("\t");
  }
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" *C \n");

  delay(5000);

}
