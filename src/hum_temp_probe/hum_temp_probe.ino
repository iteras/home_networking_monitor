#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <DHT.h>

#define DHTTYPE DHT22
#define DHTPIN 5
DHT dht(DHTPIN, DHTTYPE);
#define NB_TRYWIFI 60 // WIFI connection attempts before dumping it and going to sleep

int chk;
float temp;
float hum;

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

  //Start DHT22 module
  dht.begin();
}

void loop() {
  delay(2000);
  //Read data and store it to variables hum and temp
  hum = dht.readHumidity();
  temp = dht.readTemperature();
  //  Serial.print("Humidity: ");Serial.print(hum);Serial.print(", temperature: ");Serial.println(temp);
  Serial.print(temp); Serial.print(" "); Serial.println(hum);
  String load = "{\"humidity\":" +  String(hum) + ", \"temperature\" : " + String(temp) + ", " + "\"address\":" + "\"Pargi 1 - 16\", \"room\" : \"outdoor\"}";
  Serial.println(load);
  if (not ((hum != hum) or (temp != temp))) {
    HTTPClient http;

    http.begin("http://192.168.0.100:8000/metrics/re_post");
    http.addHeader("Content-Type", "json/application");
    int httpCode = http.POST(load);
//    delay(5000);

    String payload = http.getString();

    http.end();
  }
  ESP.deepSleep(60e6);

}
