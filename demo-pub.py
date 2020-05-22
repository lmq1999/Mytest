import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

ipaddr="192.168.122.131"
port= 1883

def on_log(client, userdata, level, buf):
    print(buf)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag=True
        print("connected")
    else:
        print("Not connected code =",rc)

        client.loop_stop()
def on_disconnect(client, userdata, rc):
    print("Client disconected")

def on_publish(client, userdata, mid):
    print("In on_pub callback mid=" ,mid)

mqtt.Client.connected_flag=False
client = mqtt.Client("python_lab_pub")
client.on_log=on_log
client.on_connect=on_connect
client.on_disconnect=on_disconnect
client.on_publish=on_publish
client.connect(ipaddr, port)
client.loop_start()

while not client.connected_flag:
    print("In wait loop")
    time.sleep(1)
time.sleep(3)
print("publish")
i=1
while i < 1000:
    publish.single("Test/test","test message qos 2",2,auth = {'username':"quan1", 'password':"123"})
    #print("published return=",publish.single)
    i += 1
    time.sleep(1)
##time.sleep(3)
##ret=client.publish("Test/test","test message qos 1",1)
##print("published return=",ret)
##time.sleep(3)
##ret=client.publish("Test/test","test message qos 2",2)
##print("published return=",ret)
time.sleep(3)
client.loop_stop()
client.disconnect()
