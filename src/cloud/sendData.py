# Publich to a ThingSpeak Channel Using MQTT
# 
# This is an example of publishing to multiple fields simultaneously.
# Connections over standard TCP, websocket or SSL are possible by setting
# the parameters below.
#
# CPU and RAM usage is collected every 20 seconds and published to a
# ThingSpeak channel using an MQTT Publish
#
# This example requires the Paho MQTT client package which
# is available at: http://eclipse.org/paho/clients/python
import paho.mqtt.publish as publish
import string


class Connection:
    # The ThingSpeak Channel ID.
    # Replace <YOUR-CHANNEL-ID> with your channel ID.
    def __init__(self):
        self.channel_ID = "1905459"#"<YOUR-CHANNEL-ID>"
        
        # The hostname of the ThingSpeak MQTT broker.
        self.mqtt_host = "mqtt3.thingspeak.com"

        # Your MQTT credentials for the device
        self.mqtt_client_ID = None
        self.mqtt_username  = None
        self.mqtt_password  = None

        self.__getCredentials()

        self.t_transport = "websockets"
        self.t_port = 80

        # Create the topic string.
        self.topic = "channels/" + channel_ID + "/publish"

        self.temperature = 0
        self.humidity = 0
        self.dominant_color = 0

    def __getCredentials(self):
        f = open('cred.config', 'r')
        t = []
        for line in f:
            t = f.split(',')
        self.mqtt_client_ID = t[1]
        self.mqtt_username  = t[3]
        self.mqtt_password  = t[5]

    def getSensorsData(self, dht_data, camera_data):
        self.temperature = dht_data["Temperature"]
        self.humidity = dht_data["Humidity"]
        self.dominant_color = camera_data


    def EstablishConnection(self):
        while (True):
            # build the payload string.
            payload = "field1=" + str(self.temperature) + "&field2=" + str(self.humidity) \
                + "&field3=" + str(self.dominant_color)
            # attempt to publish this data to the topic.
            try:
                print ("Writing Payload = ", payload," to host: ", mqtt_host, " clientID= ", mqtt_client_ID, " User ", mqtt_username, " PWD ", mqtt_password)
                publish.single(self.topic, payload, hostname=self.mqtt_host, transport=self.t_transport,
                               port=self.t_port, client_id=self.mqtt_client_ID,
                               auth={'username':self.mqtt_username,'password':self.mqtt_password})
            except (keyboardInterrupt):
                break
            except Exception as e:
                print (e) 
