#!python3
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected")
    else:
        print("Not connected code =",rc)

ipaddr="192.168.122.131"
client = mqtt.Client("python")
client.on_connect=on_connect
print("Connecting to service:", ipaddr)
client.loop_start()
client.connect(ipaddr)
client.publish("test/t","test")
time.sleep(60)
client.loop_stop()
client.disconnect()
