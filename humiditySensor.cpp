#include <dht.h>
#include <ros.h>                // this is the ros library
#include <std_msgs/UInt16.h>    // message type integer 16 bits for publishing analog values
#define dataPin 8               // Defines pin number to which the sensor is connected
dht DHT;                        // Creats a DHT object
std_msgs::UInt16 &humid_msg;
ros::NodeHandle node_handle;    // 
ros::Publisher humidity_publisher("humidity", &humid_msg);
void setup() {
  Serial.begin(9600);
  node_handle.advertise(humidity_publisher);
}
void loop() {
  int readData = DHT.read22(dataPin); // Reads the data from the sensor
  //float t = DHT.temperature; // Gets the values of the temperature
  float h = DHT.humidity; // Gets the values of the humidity
  // Printing the results on the serial monitor
  // Serial.print("Temperature = ");
  // Serial.print(t);
  // Serial.print(" *C ");
  Serial.print("    Humidity = ");
  Serial.print(h);
  Serial.println(" % ");
  if (h>75){
    humid_msg.data = 2
  }
  else {
    humid_msg.data = 0
  }
  humidity_publisher.publish( &humid_msg);
  node_handle.spinOnce();
  delay(2000); // Delays 2 seconds, as the DHT22 so that the sampling rate is 0.5Hz
}
