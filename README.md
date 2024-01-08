
# Building a Simple Weatherstation Using an ESP32, DHT11 Sensor, and AWS IoT Core

- Author: Manikyala_Tanuj
- Topics: _IoT, ESP32, AWS, Cloud, Grafana_
- Date: _25-07-2022_
- Approximate Time to Complete: _3 - 4 hours_

## Table of content

- [Building a Simple Weatherstation Using an ESP32, DHT11 Sensor, and AWS IoT Core](#building-a-simple-weatherstation-using-an-esp32--dht11-sensor--and-aws-iot-core)
  * [Project Overview](#project-overview)
  * [Objective](#objective)
  * [Material](#material)
  * [Computer Setup](#computer-setup)
  * [Circuit and Hardware Diagrams](#circuit-and-hardware-diagrams)
    + [DHT11](#dht11)
    + [RGBLED Lamp](#rgbled-lamp)
  * [Platform](#platform)
  * [The Code](#the-code)
  * [Data Transmittion and Connectivity](#data-transmission-and-connectivity)
  * [Data Representation](#data-representation)
  * [Final Results](#final-results)





## Project Overview

As illustrated in the following image below this project aims to build a simple weather station that records temperature and humidity using an ESP32, a DHT11 sensor, and an RGB LED lamp for debugging. The measurements are then transmitted to AWS IoT Core utilizing WIFI and the MQTT transport protocol. Furthermore, the data is automatically stored into a Timestream database so that it can be quired and represented using graphs with Grafana Cloud.

![Architecture](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/AWS_IoT.png)

## Objective

This IoT device is built to monitor the temperature and humidity of indoor environments and represent the gathered data in a readable format for the user as well as make it accessible anytime from anywhere and on any device that has access to the internet. There are also a few additional objects this project accomplishes:

1. This project aims to be used as a base for other projects and be further developed for more specific projects (e.g an automatic plant monitoring and watering system based on soil humidity).

2. This project aims to allow the transmission of other different types of data by slightly modifying the code and adding additional sensors (e.g air quality, air pressure, distance, etc).

3. Most importantly this project aims to act as an introduction to IoT, MQTT protocol, and AWS Cloud for IoT.

## Material

For the project the following Ultimate Starter Kit from Freenove was used which includes all needed components and more https://bit.ly/3AtGip3. But below the same components are also given separately from different vendors when and if available.

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Item</th>
    <th class="tg-0pky">Specifications</th>
    <th class="tg-0pky">Link Image</th>
    <th class="tg-0lax">Cost </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">ESP32-WROVER x 1</td>
    <td class="tg-0pky">Brand:Freenove<br>Manufacturer: Freenove<br>Processor brand: Espressif<br>Processor speed: 240 MHz<br>RAM: 8 MB<br>Type of computer memory: SRAM<br>Hard disk size: 4 MB<br>WIFI: Yes<br>Bluetooth: Yes<br>Wireless type: 2.4 GHz Radio Frequency<br>Voltage: 5 Voltage<br><br> <a href="https://www.espressif.com/sites/default/files/documentation/esp32-wrover_datasheet_en.pdf">More information</a><br></td>
    <td class="tg-0pky"><a href="https://bit.ly/3pA8h01">
         <img alt="esp32" src="images\esp32.jpg"
         width=299" height="360">
      </a></td>
    <td class="tg-0lax">149,00kr</td>
  </tr>
  <tr>
    <td class="tg-0pky">ESP32 GPIO Extension Board x 1<br></td>
    <td class="tg-0pky">--&gt;</td>
    <td class="tg-0pky"><img src="images\gpio.png" alt="gpio"
    width=323" height="360"> </td>
    <td class="tg-0lax">Included when buying Freenove pack. Not sold seperately. Can be replaced by other extension boards for esp32<br></td>
  </tr>
  <tr>
    <td class="tg-0pky">DHT11 Sensor x 1</td>
    <td class="tg-0pky">Humidity measurement range: 20-90%RH (temperature compensation 0-50℃)<br>Temperature range: 0-50℃<br>Humidity measurement accuracy: ±5.0 %RH<br>Temperature measurement accuracy: ± 2 ℃<br>Response time: &lt;5 seconds<br>Size: 1.6 x 1.2 x 0.6 cm</td>
     <td class="tg-0pky"><a href="https://bit.ly/3zYa6bT">
         <img alt="DHT11" src="images\DHT11_pic.jpg"
         width=299" height="360">
      </a></td>
    <td class="tg-0pky">109,99kr for 5</td>
  </tr>
    <tr>
    <td class="tg-0lax">Freenove RGB LED Module x 1</td>
    <td class="tg-0lax">8 Leds<br>3.5V~5.5v<br></td>
    <td class="tg-0pky"><img src="images\rgbled.jpg" alt="rgbled"
    width=199" height="176"> </td>
    <td class="tg-0lax">Included when buying Freenove pack. Not sold seperately. Can be replaced by other neopixel leds<br></td>
  </tr>
  <tr>
    <td class="tg-0pky">Jumper Wire Female to Male x 3</td>
    <td class="tg-0pky">Length: 20 cm<br>2.54 mm socketcomposition of copper and aluminum<br></td>
    <td class="tg-0pky"><a href="https://bit.ly/3w48Y57">
         <img alt="jmp_FM" src="images\JMP_FM.jpg"
         width=300" height="200">
      </a></td>
    <td class="tg-0pky">59,99kr for 40</td>
  </tr>
  <tr>
  <tr>
    <td class="tg-0pky">Jumper Wire Male to Male x 4</td>
    <td class="tg-0pky">size:Cables of different lengths (25 cm / 20 cm / 16 cm / 12 cm)<br>Material:Copper wire</td>
    <td class="tg-0pky"><a href="https://bit.ly/3K7bjlT">
         <img alt="jmp_MM" src="images\JMP_MM.jpg"
         width=300" height="200">
      </a></td>
    <td class="tg-0pky">69,99kr for 65<br></td>
  </tr>
   <tr>
    <td class="tg-0pky">Resistor 10kΩ x 1<br></td>
    <td class="tg-0pky">Resistance: 10K ohms<br>Carbon film opponent<br>Tolerance: 5%</td>
    <td class="tg-0pky"><a href="https://bit.ly/3C4LG2X">
         <img alt="resistor" src="images\resistor.jpg"
         width=300" height="200">
      </a></td>
    <td class="tg-0pky">27,06kr for 50<br></td>
  </tr>
   <tr>
    <td class="tg-0pky">Breadboard x 1<br><br></td>
    <td class="tg-0pky">Interconnect all components using 21-26 AWG wire<br>PCB board size: 3.2 x 2.1 x 0.3 inch / 8.2 x 5.5 x 1 cm<br></td>
    <td class="tg-0pky"><a href="https://bit.ly/3dtEd3g">
         <img alt="resistor" src="images\breadboard.jpg"
         width=300" height="200">
      </a></td>
    <td class="tg-0pky">135,00kr for 4<br></td>
  </tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax"></td>
  </tr>
</tbody>
</table>     

## Computer Setup

For the code development of this project is done on a Windows machine using Thonny which is an open-source python IDE with a simple interface but great features making it a great option for beginners. To download and install Thonny follow the guide on the official website: https://thonny.org . The next step is to connect your ESP32 device to your computer using a USB cable. Afterward, it should be made sure that the computer has the CH340 driver installed. If the Driver is installed “USB-SERIAL CH340 (COMx)” should be visible under the port when going to "This PC" -> "Manage" -> "Device Manager" -> "Ports (COM & LPT)" as seen in the picture below.

![COMx](https://github.com/TanujManikyala/Weatherstationnblob/main/images/port.jpg)

---

If not then the driver can be downloaded from here: https://www.wch-ic.com/search?q=CH340&t=downloads. 
Afterward, in order to run Python programs on ESP32, firmware must be burned first. For this project version v1.18 (2022-01-17) .bin can be downloaded from the official micropython webpage here: https://micropython.org/download/esp32spiram/. Once the firmware is download Thonny is used to burn it into the ESP32 (must be connected with USB to the computer) as illustrated in the following images.

![burning_firmware_1](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/burning_firmware_1.png)


![burning_firmware_2](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/burning_firmware_2.jpg)


![burning_firmware_3](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/burning_firmware_3.jpg)

---

Now the device is ready for files to be uploaded. Files can be uploaded from Thonny as shown in the next image.

![uploading_files](https://github.com/TanujManikyala/Weatherstationn/images/uploading_files.png)

## Circuit and Hardware Diagrams

This section contains circuit and hardware diagrams for the project. Diagrams for the DHT11 sensor and the RGB LED Lamp are separated for visibility and readability purposes. All information regarding how the electronics are connected, wiring, resistors, current, and voltage can be found in the diagrams. This setup is only for development purposes and is not to be used in production. The complete real-life setup containing both can be viewed in the section Final results [link](#final-results)

### DHT11

![DHT11](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/DHT11.png)

1. VCC Power supply pin (within the range 3.3V-5.5V).
2. SDA Data pin used to communicate with other devices.
3. NC Has no functional purpose used during manufacturing and testing of the sensor.
4. GND Pin for Grounding.

---

![circuit_diagram_DHT11](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/circuit_diagram_DHT11.png)

---

![material_DHT11](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/material_DTH11.png)

![hardware_connection_DHT11](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/hardware_connection_diagram_DHT11.jpg)



### RGBLED Lamp

![RGBLED_lamp](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/RGBLED_Lamp.jpg)

1. S Pin for input control signal.
2. V Power suply pin (+3.5V~5.5V ).
3. G Pin for grounding (GND).

---

![circuit_diagram_RGBLED](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/circuit_diagram_RGBLEDLamp.png)

---

![material_RGBLED](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/material_RGBLED.jpg)

![hardware_connection_RGBLED](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/hardware_connection_diagram_RGBLEDLamp.jpg)



## Platform

This project's platform of choice is AWS cloud and specifically AWS IoT Core. AWS IoT Core allows connected devices to easily and securely communicate with other devices, applications, and services. Moreover, IoT Core allows for the creation of IoT applications that gather, process, respond and act on data without having to manually manage any infrastructure. Additionally, AWS IoT Core provides great scalability by supporting billions of devices and trillions of messages depending on the paid plan but for this project the free tier is used which allows for a certain free number of message transmissions each month. 

An alternative to AWS Cloud or a cloud service provider, in general, would be a self-hosting local platform installation using Dockers and TIG stack. Although using a local solution would remove any need for paid subscriptions and would increase privacy regarding the user's data it also has some downsides which go against this project's objectives. First, hosting a local TIG stack would not allow for the data to be accessed from anywhere and any device (with the proper credentials) because it is limited to devices in the same network. Second, the platform would be probably hosted on a personal computer that most users won't be willing to have operating 24/7 thus not allowing for the data to be accessed at any time but only when the user's machine is powered on and operating. That being said there are also other cloud providers out there but another reason AWS cloud was chosen is that it's tried and tested with an active community and a lot of guides and supports available.

The following officila guide can be followed to create an AWS account (https://docs.aws.amazon.com/iot/latest/developerguide/setting-up.html)


## The Code

The project's code is written in micropython and it can be found in the [WeatherStation.py](https://github.com/TanujManikyala/Weatherstationn/WeatherStation.py) file with some comments on what each function is supposed to do. Having said that there is one function that might be worth mentioning here because it has to do with connecting AWS IoT Core:

The function below first opens and reads the certification and key files downloaded from the user AWS account and uses them as SSL_parameters to set up the MQTT_PORT (port) and together with the provided MQTT_CLIENT_ID (client id), MQTT_HOST (server) are used as an argument to establish a client connection to AWS IoT Core. If any of the previous arguments are incorrect or for some reason it cants establish a connection an exception is raised. 

Credits: https://forum.micropython.org/viewtopic.php?t=5166

```python
from umqtt.simple import MQTTClient

# AWS cert and key.
CERT_FILE = "/esp32_weatherStation.cert.pem"
KEY_FILE = "/esp32_weatherStation.private.key"

# AWS Endpoints
MQTT_CLIENT_ID = "basicPubSub"
MQTT_PORT = 8883

MQTT_HOST = "********" #ENTER YOUR MQTT HOST HERE


mqtt_client = None

def connect_mqtt():    
    global mqtt_client

    try:
        with open(KEY_FILE, "r") as f: 
            key = f.read()

        print("Key OK!")
            
        with open(CERT_FILE, "r") as f: 
            cert = f.read()

        print("Cert OK!")

        mqtt_client = MQTTClient(client_id=MQTT_CLIENT_ID, server=MQTT_HOST, port=MQTT_PORT, keepalive=5000, ssl=True, ssl_params={"cert":cert, "key":key, "server_side":False})
        mqtt_client.connect()
        print('MQTT Connected!')

        
    except Exception as e:
        print('Cannot connect to MQTT: ' + str(e))
        raise
```


## Data Transmission and Connectivity

As previously mentioned the program uses the MQTT (Message Queue Telemetry Transmission) protocol to transmit the temperature and humidity measurements to AWS IoT Core. In the provided code the data is transmitted approximately every 100000 ms which is the time the device spends sleeping after every transmission but it can be easily modified according to one's needs. The following official tutorial can be used to set up everything up on the cloud and create a broker and topic (server) so the device (client) can start publishing data to it: iot quick connect (https://docs.aws.amazon.com/iot/latest/developerguide/iot-quick-start.html) note the certification and key files obtain by following the guide must be uploaded to the ESP32. 

MQTT was preferred over other transport protocols such as HTTP, UDP, etc for a few reasons. First, MQTT ensures message delivery. MQTT is built on top of TCP/IP which establishes a client-server connection and after every packet is sent it will wait for an acknowledgment packet back otherwise it will retransmit [https://www.fortinet.com/resources/cyberglossary/tcp-iph]. Additionally, MQTT implements QoS (Quality of Service) further increasing data transmission reliability (QoS 0: At most once delivery, QoS 1: At least once delivery, Qos 2: Exactly once delivery). Since IoT devices could be battery-powered, constantly moving, or operating in harsh environments network connections can become unstable thus, it is important to maximize the chances of messages getting delivered.
Second, MQTT is lightweight. MQTT can run on small, cheap devices since MQTT headers are typically only about 2 bytes while for example, an HTTP header is around 8000 bytes. Last but not least, MQTT is battery friendly. The MQTT protocol was developed to operate in harsh unwelcoming environments where access to electricity wasn't available. For example, devices using the MQTT protocol consume 47 times less energy on WIFI and 170 times less on 3G compared to when using HTTP. Despite the pros, there are certain drawbacks to MQTT such as issues with latency and no built-in security but they are not a major focus of this project.

The client-side implements the below function to transmit the data after it has connected using the function mentioned in the previous section ('The Code'). The function uses the micropythons umqtt.simple library and specifically the MQTTClient.publish() function which takes the topic and a message as parameters.

```python

from umqtt.simple import MQTTClient

MQTT_TOPIC = "sdk/test/Python"

mqtt_client = None

# Function used to publish a message to AWS IoT core
def pub_msg(msg):
    global mqtt_client
    try:    
        mqtt_client.publish(MQTT_TOPIC, msg)
        print("Sent: " + msg)
    except Exception as e:
        print("Exception publish: " + str(e))
        raise

```

Since the data needs to be transmitted in JSON format the following code is used to convert the DHT11 sensor measurements into JSON format by using the . dumps(data) method from micropythons json library.

```python

import machine
import dht
import json

pin = machine.Pin(2, machine.Pin.OUT)

DHT = dht.DHT11(machine.Pin(13))

 # Measure temperature and humidity
DHT.measure()

# Cast DHT11 measurements to JSON format so it can be sent.
data = {"temperature": DHT.temperature(), "humidity": DHT.humidity(), "device_id": "sensor_1"}
msg = json.dumps(data)

```

Of course, for the data to be sent to the cloud a wireless protocol needs to be used for the transmission to be possible and in this case, it is WIFI. WIFI is chosen because it is widely available, cheap, and fast. A 2.4 GHz connection can better penetrate solid objects and offer speeds up to 150 Mbps. A major drawback of using a WIFI connection is power consumption. The average battery lifespan for 2.4 GHz is 8-9 hours which is not suitable for IoT devices and sensors that might require weeks and years of battery. Furthermore, WIFI is not the best option when a wider area of coverage is needed. Despite that this project is mostly destinated for indoor environments meaning that a power supply can be available at all times. If a wider area coverage is important as well as power consumption an LPWAN (low-power WAN) wireless protocol such as LoRa would be a better choice offering both lower power consumption and a range of 10km in urban areas and around double the amount in the open (keep in mind that it would require a device that supports LoRa as the ESP32 used in this project doesn't). The following function allows the device to connect to a 2.4 GHz network. Micropythons network library and its functions are used to establish the connection provided the WIFI network SSID and password are provided.

```python

import network

# WIFI Credinentials
WIFI_SSID     = '*******' #Enter the router name
WIFI_PW = '*******' #Enter the router password


# Function used to connect to WIFI
def STA_Setup(WIFI_SSID,WIFI_PW):
    print("Setup start\n")
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to',WIFI_SSID)
        sta_if.active(True)
        sta_if.connect(WIFI_SSID,WIFI_PW)
        while not sta_if.isconnected():
            pass
    print('WIFI Connected!, IP address:', sta_if.ifconfig())

```

## Data Representation

After each message publishing or in other words data transmission the client device goes to sleep for 100000 ms. After the device wakes up from sleep it then repeats the whole process meaning it connects to the WIFI and MQTT server, it measures the humidity and temperature, publishes the data, and goes to sleep again. 

All values received by AWS IoT Core are automatically saved to an AWS Timestream database. The data stored can be preserved until storage space runs out or some other policy of choice (storage can auto-scale depending on the plan y choose). Older data is automatically backed up into a separate magnetic store despite that, you can still query both recent and historical data from the same tools and interfaces since the timestreams query engine combines recent and historical data without having to specify the data location. There are plenty of other options concerning data persistence when setting up the Timestream but for this project, the most minimal options were selected to keep the costs as low as possible or free tier. There are several other reasons why Timestream is the database of choice for this project. Timestream is a fast, encrypted, serverless, and auto-scalable time series database that doesn't require any infrastructure management. It can quickly analyze time series data with SQL which makes it great for IoT applications. Moreover, it has the option to identify data trends and patterns in near real-time.

The data stored on the database are then queried using Grafana Cloud and the results are represented in the form of graphs as illustrated below.

![Graphs](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/graphs.png)

For more info on how to connect Timestream to AWS IoT Core and use Grafana Cloud to represent the data follow this picture guide [here](https://github.com/TanujManikyala/Weatherstationn/blob/main/TimeStream_Grafana_SetUp.md)

## Final Results

The following pictures illustrate the ESP32 with all the parts put together.

![Final_Result_1](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/microcontroller_1.jpg)

![Final_Result_2](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/microcontroller_2.jpg)

---
Messages arriving in AWS IoT Core

![aws_mqqt](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/iot_mqqt.png)

---
Data representation in Grafana.

![data_graph](https://github.com/TanujManikyala/Weatherstationn/blob/main/images/graphs.png)

The whole process of creating the project went smoothly and no major problems occurred during the development of either hardware or software. Some things that could have been done differently would be upgrading to a microcontroller with LORA support as well as updating the sensors to build a resilient enough outdoor weather station.
