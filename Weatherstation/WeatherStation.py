import machine
import network
from umqtt.simple import MQTTClient
import json
import dht
import neopixel
import time

pin = machine.Pin(2, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 8)

DHT = dht.DHT11(machine.Pin(13))

# Brightness :0-255
brightness=10                                
colors=[[brightness,0,0],                    #red
        [0,brightness,0],                    #green
        [0,0,brightness],                    #blue
        [brightness,brightness,brightness],  #white
        [0,0,0]] #close
    
sleep_time_ms = 100000

# REPLACE THE VARIABLES BELOW WITH YOUR OWN INFO WHERE NEEDED.

# WIFI Credinentials
WIFI_SSID     = '*******' #Enter the router name
WIFI_PW = '*******' #Enter the router password

# AWS cert and key.
CERT_FILE = "/esp32_weatherStation.cert.pem"
KEY_FILE = "/esp32_weatherStation.private.key"

# AWS Endpoints
MQTT_CLIENT_ID = "basicPubSub"
MQTT_PORT = 8883
MQTT_TOPIC = "sdk/test/Python"

MQTT_HOST = "********" #ENTER YOUR MQTT HOST HERE


mqtt_client = None

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
    
 
# Function used to read the AWS certifications and key files and connect to AWS IoT core
# https://forum.micropython.org/viewtopic.php?t=5166
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
 
# Function used to publish a message to AWS IoT core
def pub_msg(msg):
    global mqtt_client
    try:    
        mqtt_client.publish(MQTT_TOPIC, msg)
        print("Sent: " + msg)
    except Exception as e:
        print("Exception publish: " + str(e))
        raise

# Function to flash the neo leds with a given color.
def neo_leds(color):
    for j in range(0,8):
            np[j]=color
            np.write()
            time.sleep_ms(50)
    time.sleep_ms(500)

    
#Main Loop
while True:
        try:
            # Connect to WIFI.
            STA_Setup(WIFI_SSID,WIFI_PW)
            neo_leds(colors[3])
            
            # Connect to MQTT broker.
            connect_mqtt()
            neo_leds(colors[2])
            
            # Measure temperature and humidity
            DHT.measure()
            
            # Cast measured data to JSON format so it can be sent.
            data = {"temperature": DHT.temperature(), "humidity": DHT.humidity()
                    , "device_id": "sensor_1"}
            msg = json.dumps(data)
        
            # Publish MQTT message.
            pub_msg(msg)
            neo_leds(colors[1])
            neo_leds(colors[4])
            
        except:
            sta_if.disconnect()
            neo_leds(colors[0])
            

        print("\nGoing to sleep\n")
        machine.deepsleep(sleep_time_ms)
    
    


