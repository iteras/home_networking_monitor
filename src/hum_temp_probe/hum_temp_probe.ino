#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <DHT.h>

#define DHTTYPE DHT22
int DHTPIN = 04;
DHT dht(DHTPIN,DHTTYPE);

int chk;
float temp;
float hum;

const char* ssid = "      "; //your WiFi Name
const char* password = "52101ehhf16";  //Your Wifi Password
void setup() {
  Serial.begin(115200);
  delay(10); 

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  //Start DHT22 module
  dht.begin();
}

void loop() {
  delay(2000);
  //Read data and store it to variables hum and temp
  hum = dht.readHumidity();
  temp= dht.readTemperature();
  Serial.print("Humidity: ");Serial.print(hum);Serial.print(", temperature: ");Serial.println(temp);
  if (not ((hum != hum) or (temp != temp))){
    HTTPClient http;
    
    http.begin("http://192.168.0.100:8080/metrics/"); //TODO: APPLY CORRECT URL
    http.addHeader("Content-Type", "json/application");
    //String load =  //TODO: Apply corred load
    int httpCode = http.POST(load);
    
    String payload = http.getString();
    
    http.end
  }
  
 }
