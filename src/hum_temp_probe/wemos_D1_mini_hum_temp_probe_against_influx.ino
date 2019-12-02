#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <CircularBuffer.h>
#define NB_TRYWIFI 60 // WIFI connection attempts before dumping it and going to sleep



byte NTCPin = A0;
#define SERIESRESISTOR 9400
#define NOMINAL_RESISTANCE 10000
#define NOMINAL_TEMPERATURE 25
#define BCOEFFICIENT 3470

CircularBuffer<float,20> floats;
int chk;
float temp;

const char* ssid = "      "; //your WiFi Name
const char* password = "52101ehhf16";  //Your Wifi Password
void setup() {
  Serial.begin(115200);
  delay(10);

  // Connect to Wi-Fi
  int _try = 0;
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    _try++;
    Serial.println("Wifi not starting");
    if (_try >= NB_TRYWIFI) {
      ESP.deepSleep(60e6);
    }
  }

}

void loop() {
  delay(100);
  //Read data and store it to variables hum and temp


  float ADCvalue;
  float Resistance;

  for(int i = 0; i < 20; i++){
    ADCvalue = analogRead(NTCPin);
//    Serial.print("Analoge ");
//    Serial.print(ADCvalue);
//    Serial.print(" = ");
    //convert value to resistance
    Resistance = (1023 / ADCvalue) - 1;
    Resistance = SERIESRESISTOR / Resistance;
//    Serial.print(Resistance);
//    Serial.println(" Ohm");
    float steinhart;
  //  steinhart = Resistance / NOMINAL_RESISTANCE; // (R/Ro)
    steinhart = NOMINAL_RESISTANCE / Resistance; // (R/Ro)
    steinhart = log(steinhart); // ln(R/Ro)
    steinhart /= BCOEFFICIENT; // 1/B * ln(R/Ro)
    steinhart += 1.0 / (NOMINAL_TEMPERATURE + 273.15); // + (1/To)
    steinhart = (1.0 / steinhart); // Invert
    steinhart -= 273.15; // convert to C
    temp = steinhart -3;
    if (floats.size() >= 20) {
      floats.pop();
      floats.unshift(temp);
    } else {
      floats.unshift(temp);
    }
    delay(100);
  }
  float sum = 0;
  for (int i = 0; i < floats.size(); i++){
    sum = sum + floats[i];
  }
  float T = sum / floats.size();

  String load = "{\"temperature\" : " + String(T) + ",\"humidity\" : -1, \"address\":" + "\"Pargi 1 - 16\", \"room\" : \"outdoor\"}";
  Serial.println(load);
//  if (T != T) {
  Serial.println("posting");
  HTTPClient http;

  http.begin("http://192.168.0.100:8000/metrics/re_post");
  http.addHeader("Content-Type", "json/application");
  int httpCode = http.POST(load);
//    delay(5000);

  String payload = http.getString();

  http.end();
//  }
  //delay(5000);
  ESP.deepSleep(60e6);
}