import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("UCC/pihealth")

	
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

	
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("82.165.16.151", 1883, 60)

client.loop_forever()

# how to publish to channel
 mosquitto_pub -h 82.165.16.151 -m "Rey $(./monitor.py)" -t UCC/pihealth

#how to subscribe to channel: first go to your root
 mosquitto_sub -h 82.165.16.151 -t UCC/pihealth 

# global_code_files
